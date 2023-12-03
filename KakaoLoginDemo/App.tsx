import React from 'react';
import { SafeAreaView, Text, View, Pressable } from 'react-native';
import * as KakaoLogin from "@react-native-seoul/kakao-login";
import axios from 'axios';

function App() {
  const signInWithKakao = async () => {
    try {
      // Fetch information of current user from Kakao, using access token
      // received from Kakao Login API.
      // Refer to:
      // https://developers.kakao.com/docs/latest/ko/kakaologin/rest-api#req-user-info
      const loginData = await KakaoLogin.login()
        .then((res) => res.accessToken)
        .then((token) => axios.get(
            "https://kapi.kakao.com/v2/user/me",
            {
              headers: {
                "Authorization": `Bearer ${token}`,
                "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
              }
            }
          ).then((res) => res.data)
        );
      
      // Login user to FastAPI server using Kakao user ID
      const username = await axios.post(
        "http://localhost:8000/login/",
        loginData
      ).then((res) => res.data);
      console.log(username);
    } catch(err) {
      console.log("Login error", err);
    }
  };

  return (
    <SafeAreaView>
      <Pressable onPress={() => signInWithKakao()}>
        <Text>카카오 로그인</Text>
      </Pressable>
    </SafeAreaView>
  )
}

export default App;
