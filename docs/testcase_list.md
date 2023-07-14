# TEST Case List

각 기능에 따른 테스트 케이스를 정리 합니다.


**API V1**
Base URL : `api/v1/`

| path                    | 기능            | 설명                                       | 예상 응답                            |
| ----------------------- | --------------- | ------------------------------------------ | ------------------------------------ |
| accounts/signup         | 회원가입        | 이메일, 이름, 패스워드 등 다 valid 한 경우 | <span style="color:green">200</span> |
|                         |                 | 회원가입 할 이메일이 이미 있는 경우        | <span style="color:red">400</span>   |
|                         |                 | 이메일 형식이 맞지 않는 경우               | <span style="color:red">400</span>   |
|                         |                 | 패스워드가 8자 이상이 아닌 경우            | <span style="color:red">400</span>   |
| accounts/signin         | 로그인          | 이메일, 패스워드 모두 valid 한 경우        | <span style="color:green">200</span> |
|                         |                 | 이메일에 맞는 유저가 없는 경우             | <span style="color:red">400</span>   |
|                         |                 | 패스워드가 올바르지 않는 경우              | <span style="color:red">400</span>   |
| accounts/email-check    | 이메일 체크     | 이메일이 있는 경우(Mock 필요)              | <span style="color:green">200</span> |
|                         |                 | 이메일이 없는 경우                         | <span style="color:red">400</span>   |
| accounts/reset-password | 비밀번호 재설정 | 토큰, 비밀번호가 올바른 경우(Mock 필요)    | <span style="color:green">200</span> |
|                         |                 | 토큰이 올바르지 않은 경우                  | <span style="color:red">400</span>   |
|                         |                 | 비밀번호가 올바르지 않은 경우              | <span style="color:red">400</span>   |
| accounts/withdrawal     | 회원탈퇴        | 유저가 로그인 된 경우                      | <span style="color:green">204</span> |
|                         |                 | 유저가 로그인 되지 않은 경우               | <span style="color:red">401</span>   |

