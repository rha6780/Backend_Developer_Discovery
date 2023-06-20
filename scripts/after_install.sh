#!/bin/bash

# ECR 로그인
aws ecr get-login-password --region ap-northeast-2 | docker login --username AWS --password-stdin 164899418867.dkr.ecr.ap-northeast-2.amazonaws.com/developer_discovery_repository

# Docker 컨테이너 정지 및 삭제
docker stop developer_discovery
docker rm developer_discovery

# ECR 이미지 가져오기
docker pull 164899418867.dkr.ecr.ap-northeast-2.amazonaws.com/developer_discovery_repository:latest

# Docker 컨테이너 실행
docker run -d -it --name developer_discovery -p 80:80 164899418867.dkr.ecr.ap-northeast-2.amazonaws.com/developer_discovery_repository:latest
