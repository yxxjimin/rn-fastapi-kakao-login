React Native / FastAPI demo project for testing [Kakao Login](https://developers.kakao.com/docs/latest/ko/kakaologin/common#intro) with [@react-native-seoul/kakao-login](https://github.com/crossplatformkorea/react-native-kakao-login).

## Flow
```mermaid
sequenceDiagram
    participant R as React Native
    participant F as FastAPI
    participant AU as Kakao Auth
    participant AP as Kakao API
    participant D as Database

    R ->>+ AU: Request Kakao Login
    AU ->>- R: Return Access Token

    R ->>+ F: POST /login/
    F ->>+ AP: GET https://kapi.kakao.com/v2/user/me/
    AP ->>- F: { "id": int, "connected_at": str }
    F ->>+ D: Find user by ID
    D ->>- F: Retrieve username
    F ->>- R: Username
```
