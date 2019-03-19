# Use an official Python runtime as a parent image
FROM python:3.7-alpine
# FROM python:3.7.2

# RUN apk add --no-cache --virtual .build-deps gcc musl-dev
RUN apk add build-base
RUN apk add libffi-dev openssl-dev

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