#!/bin/bash
docker_image="gabrielrih/devops-demo-app:latest"

echo "Getting image $docker_image"
docker pull $docker_image

echo "Printing images for debugging"
docker image ls

echo "Starting a container for testing"
docker run --rm -d -p 5000:5000 $docker_image

echo "Listing the running containers and listener"
docker container ls

echo "Open ports"
netstat -nat | grep 5000

# echo "Run curl for test connection"
# curl http://localhost:5000/api/food/

echo "Run integration tests"
pytest test/integration