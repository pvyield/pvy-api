# Use an official Python runtime as a parent image
FROM python:3.7-alpine
# FROM tiangolo/meinheld-gunicorn:python3.7-alpine3.8

RUN apk add build-base
RUN apk add libffi-dev openssl-dev
#RUN apk add nginx

# copy requirements only to use caching
COPY requirements.txt /app/requirements.txt

# install python packages
RUN pip install -r /app/requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]