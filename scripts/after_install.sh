#!/bin/bash


# Deprecated
# # ECR 로그인
aws ecr get-login-password --region ap-northeast-2 | docker login --username AWS --password-stdin 164899418867.dkr.ecr.ap-northeast-2.amazonaws.com/developer_discovery_repository

# # Docker 컨테이너 정지 및 삭제
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images -q)

# # ECR 이미지 가져오기
docker pull 164899418867.dkr.ecr.ap-northeast-2.amazonaws.com/developer_discovery_repository:latest

# # Web Docker 컨테이너 실행
docker run -d -it --name developer_discovery-web-1 -p 3000:3000 164899418867.dkr.ecr.ap-northeast-2.amazonaws.com/developer_discovery_repository:latest

# docker exec -i $(sudo docker ps -q -l) python developer_discover/manage.py migrate


# Git pull
cd /root/projects/Backend_Developer_Discovery

git pull

docker compose -f docker-compose-prod.yml up -d nginx api
