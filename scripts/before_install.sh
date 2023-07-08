sudo apt-get update

sudo apt-get install ruby
sudo apt-get install wget

sudo apt-get install awscli

# cd /home/ubuntu
# sudo wget https://aws-codedeploy-ap-northeast-2.s3.ap-northeast-2.amazonaws.com/latest/install

# # 설치 파일에 실행 권한 부여
# sudo chmod +x install

# # 설치 진행 및 Agent 상태 확인
# sudo install auto
# sudo service codedeploy-agent status

# # 우분투 Docker 설치
# sudo apt-get install \
#     ca-certificates \
#     curl \
#     gnupg

# sudo mkdir -m 0755 -p /etc/apt/keyrings
# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg


# echo \
#   "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
#   "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
#   sudo tee /etc/apt/sources.list.d/docker.list > /dev/null


# sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
