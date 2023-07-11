# Backend Developer Discovery

[![Coverage Status](coverage-badge.svg?dummy=8484744)](./reports/coverage/index.html)


## 프로젝트 소개
개발의 유용한 정보를 모아두는 사이트로 Discovery 에 영감을 받아 작업합니다.

<br>

### 전체 구조

![DeveloperDiscovery](./docs/DeveloperDiscovery_with_nginx.png)

EC2 내부에 Nginx, Django, Next.js가 도커 컨테이너로 실행됩니다. Nginx를 통해 healthcheck와 라우팅을 설정합니다. SSR 방식이고 각 페이지에 대한 요청은 Django 로 전송됩니다. 여기서 렌더링 중 필요한 js, css는 Next.js에서 응답하게 됩니다. 기능적인 부분과 테스트, 문서화를 더 보충한 이후에 캐싱 및 최적화를 진행할 예정입니다.

<br>

**구조 개선**

- 이슈 : Django DEBUG=False 옵션에서 static, media, Next.js 페이지와 각종 이미지 제공 안됨.
  - 해결 : Nginx 도입

- 이슈 : 페이지 렌더링 시간이 오래걸림
  - 원인 : 기존 Vercel을 이용하게 되면, 각각 다른 네트워크에 있는 서버로 `EC2` <=> `Vercel` 사이에 통신이 많은 점
  - 해결 : Nginx를 통한 EC2 내부 컨테이너 간의 통신으로 변경 및 캐싱 적용


Nginx를 도입함으로 백엔드, 프론트의 배포 과정, 비용을 일관성있게 관리할 수 있다. 다만, 이미지 빌드에서 메모리가 부족해 빌드 도중 멈추는 이슈가 있기 때문에 도커 이미지 최적화가 필요하다.

<br>

<details>
<summary>기존 배포 구조(deprecated)</summary>

웹페이지는 SSR 방식으로 프론트 부분은 Vercel 서버에 배포하고, 이를 EC2에 올라가 있는 Django에서 렌더링 합니다. 회원 로직과 게시판이 주 기능으로 마크다운 에디터를 사용하고, 글에 추가되는 이미지는 S3에 업로드 합니다. 관련 프론트와 인프라는 아래 연계 프로젝트에서 진행합니다.

![DeveloperDiscoveryDeprecated](./docs/DeveloperDiscovery_deprecated.png)

</details>

<br>

### 연계 프로젝트

- 프론트 
  - [FrontendDeveloperDiscovery](https://github.com/rha6780/Frontend_Developer_Discovery)
  - Typescript, Next.js

- 인프라
  - [InfraDeveloperDiscovery](https://github.com/rha6780/Infra_Developer_Discovery) 
  - Terraform, AWS


<br>

## Architecture

### DB ERD
![Developer Discovery](./docs/Developer%20DiscoveryDBERD.png)

<br>

## 개발 환경

<details>
<summary>환경 구성</summary>

- Python 3.10
- 다음 명령어를 순차적으로 실행하여 환경 구성을 합니다.
- git clone 프로젝트_CLONE_URL
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

</details>

<details>
<summary>coverage</summary>

- 로컬에서 환경 구성 이후 developer_discover 폴더에서 coverage run manage.py test 를 통해 현재 커버리지를 알 수 있습니다. 로컬 개발 시 수시로 확인해서 80% 를 목표로 테스트 코드를 작성합시다.
- [coverage](https://coverage.readthedocs.io/en/latest/index.html) 및 [badge](https://smarie.github.io/python-genbadge/) 관련 문서를 참고하세요.
- TODO: github action으로 coverage 뱃지 업데이트 자동화하기

**수동 업데이트**
- 프로젝트 루트에서 `cd developer discover`
- 이전에 테스트한 결과가 있는 경우, `coverage erase`
- `coverage run manage.py test` 를 통해 테스트
- `coverage xml && coverage html` 로 각각 파일 생성
- `mv coverage.xml ../reports/coverage` html의 경우 htmlcov 에서 index를 coverage 폴더로 이동
- 프로젝트 루트에서 `genbadge coverage`로 뱃지 업데이트

</details>
