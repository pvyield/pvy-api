#!/usr/bin/env bash

# more bash-friendly output for jq
JQ="jq --raw-output --exit-status"

configure_aws_cli(){
	aws --version
	aws configure set default.region $AWS_DEFAULT_REGION
	aws configure set default.output json
}

deploy_cluster() {

    clustername="$AWS_RESOURCE_NAME_PREFIX-cluster"
    servicename="$AWS_RESOURCE_NAME_PREFIX-service"
    containername=$servicename # "$AWS_RESOURCE_NAME_PREFIX-container"
    executionrole="$AWS_RESOURCE_NAME_PREFIX-ecs-execution-role"
    family=$servicename

    make_task_def
    register_definition
    if [[ $(aws ecs update-service --cluster $clustername --service $servicename --task-definition $revision | \
                   $JQ '.service.taskDefinition') != $revision ]]; then
        echo "Error updating service."
        return 1
    fi

    # wait for older revisions to disappear
    # not really necessary, but nice for demos
    #for attempt in {1..30}; do
    #   if stale=$(aws ecs describe-services --cluster $clustername --services $servicename | \
    #                   $JQ ".services[0].deployments | .[] | select(.taskDefinition != \"$revision\") | .taskDefinition"); then
    #        echo "Waiting for stale deployments:"
    #        echo "$stale"
    #        sleep 5
    #    else
    #        echo "Deployed!"
    #        return 0
    #    fi
    #done
    #echo "Service update took too long."
    #return 1
}

make_task_def() {
    task_template='{
            \"requiresCompatibilities\": [
                \"FARGATE\"
            ],
            \"containerDefinitions\": [
                {
                    \"name\": \"%s\",
                    \"image\": \"%s.dkr.ecr.%s.amazonaws.com/%s:%s\",
                    \"memoryReservation\": 512,
                    \"cpu\": 256,
                    \"memory\": 512,
                    \"essential\": true,
                    \"portMappings\": [
                        {
                            \"containerPort\": 8080,
                            \"hostPort\": 8080,
                            \"protocol\": \"tcp\"
                        }
                    ]
                }
            ],
            \"networkMode\": \"awsvpc\",
            \"memory\": \"512\",
            \"cpu\": \"256\",
            \"executionRoleArn\": \"%s\",
            \"family\": \"%s\"
        }'

    task_def=$(printf "$task_template" $containername $AWS_ACCOUNT_ID $AWS_DEFAULT_REGION $AWS_RESOURCE_NAME_PREFIX $CIRCLE_SHA1 $executionrole $family)
}

push_ecr_image(){
    eval $(aws ecr get-login --region $AWS_DEFAULT_REGION --no-include-email)
    docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$AWS_RESOURCE_NAME_PREFIX:$CIRCLE_SHA1
}

register_definition() {
    echo "task-definitions: $task_def"
    if revision=$(aws ecs register-task-definition --cli-input-json "$task_def" | $JQ '.taskDefinition.taskDefinitionArn'); then
        echo "Revision: $revision"
    else
        echo "Failed to register task definition"
        return 1
    fi
}


configure_aws_cli
push_ecr_image
deploy_cluster