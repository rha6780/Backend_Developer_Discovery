# Backend Developer Discovery 개발

[![Coverage Status](coverage-badge.svg?dummy=8484744)](.)

- [Frontend 프로젝트](https://github.com/rha6780/Frontend_Developer_Discovery) 의 API를 주로 구성합니다.
- Frontend는 SSR로 제공됨으로 해당 프로젝트에 node 서버 및 db 등을 docker-compose를 이용해 구성합니다.
- Infra는 Infra_Developer_Discovery 레포에서 Terraform으로 관리합니다.
- 초반에 구성한 페이지도 있습니다.


<br>

## 환경 구성
- Python 3.10
- 다음 명령어를 순차적으로 실행하여 환경 구성을 합니다.
- `pipenv install`
- `pipenv shell` 로 가상환경에 들어갑니다.
- .envs 폴더를 생성하고 폴더 안에 .dev, .prod, .test 파일을 생성합니다.
- 해당 파일들에 아래 코드를 작성합니다.
```
SECRET_KEY='시크릿 키'
POSTGRES_DB=test_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=127.0.0.1
POSTGRES_PORT=5432
```

## Architecture

### DB ERD
![Developer Discovery](https://github.com/rha6780/Backend_Developer_Discovery/assets/47859845/54dfd9c9-8850-4043-aa3f-f6690cc627c1)
