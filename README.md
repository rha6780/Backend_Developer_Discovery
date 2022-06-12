# Backend Developer Discovery
- [Frontend 프로젝트](https://github.com/rha6780/Frontend_Developer_Discovery) 의 API를 구성합니다.
- Frontend는 AWS Amplify 로 배포하고 API의 경우 EC2 또는 Lambda를 이용할 예정입니다.
- 초반에 구성한 페이지도 있습니다.


<br>
## 환경 구성
- Python 3.10
- 다음 명령어를 순차적으로 실행하여 환경 구성을 합니다.
- `pipenv install`
- `pipenv shell` 로 가상환경에 들어갑니다.
- .envs 폴더를 생성하고 폴더 안에 .dev, .prod, .test 파일을 생성합니다. 
- 해당 파일들에 아래 코드를 작성합니다.
  