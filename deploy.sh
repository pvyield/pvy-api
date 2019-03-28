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
    servicename="$AWS_RESOURCE_NAME_PREFIX-service-03"
    taskname="$AWS_RESOURCE_NAME_PREFIX-task"
    containername="$AWS_RESOURCE_NAME_PREFIX-container" # $servicename
    executionrole="$AWS_RESOURCE_NAME_PREFIX-ecs-execution-role"

    make_task_def
    register_definition
    if [[ $(aws ecs update-service --cluster $clustername --service $servicename --task-definition $taskrevision | \
                   $JQ '.service.taskDefinition') != $taskrevision ]]; then
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
            \"family\": \"%s\",
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
                            \"containerPort\": 80,
                            \"hostPort\": 80,
                            \"protocol\": \"tcp\"
                        }
                    ],
                    \"environment\" : [
                        { \"name\" : \"ENV_TYPE\", \"value\" : \"%s\" },
                        { \"name\" : \"SENTRY_DSN\", \"value\" : \"%s\" }
                    ]
                }
            ],
            \"networkMode\": \"awsvpc\",
            \"memory\": \"512\",
            \"cpu\": \"256\",
            \"executionRoleArn\": \"%s\"
        }'

    task_definition=$(printf "$task_template" $taskname $containername $AWS_ACCOUNT_ID $AWS_DEFAULT_REGION $AWS_RESOURCE_NAME_PREFIX $CIRCLE_SHA1 $ENV_TYPE $SENTRY_DSN $executionrole)
}

push_ecr_image(){
    eval $(aws ecr get-login --region $AWS_DEFAULT_REGION --no-include-email)
    docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$AWS_RESOURCE_NAME_PREFIX:$CIRCLE_SHA1
}

register_definition() {
    echo "task-definitions: $task_definition"
    if taskrevision=$(aws ecs register-task-definition --cli-input-json "$task_definition" | $JQ '.taskDefinition.taskDefinitionArn'); then
        echo "Task Revision: $taskrevision"
    else
        echo "Failed to register task definition"
        return 1
    fi
}

configure_aws_cli
push_ecr_image
deploy_cluster