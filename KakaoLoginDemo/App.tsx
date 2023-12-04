import React, { useState } from 'react';
import { SafeAreaView, Text, View, Pressable } from 'react-native';
import * as KakaoLogin from "@react-native-seoul/kakao-login";
import axios from 'axios';

function App() {
  const [user, setUser] = useState("(Not logged in)");

  // const signInWithKakao = async () => {
  //   try {
  //     // Fetch information of current user from Kakao, using access token
  //     // received from Kakao Login API.
  //     // Refer to:
  //     // https://developers.kakao.com/docs/latest/ko/kakaologin/rest-api#req-user-info
  //     const loginData = await KakaoLogin.login()
  //       .then((res) => res.accessToken)
  //       .then((token) => axios.get(
  //           "https://kapi.kakao.com/v2/user/me",
  //           {
  //             headers: {
  //               "Authorization": `Bearer ${token}`,
  //               "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
  //             }
  //           }
  //         ).then((res) => res.data)
  //       );
      
  //     // Login user to FastAPI server using Kakao user ID
  //     const username = await axios.post(
  //       "http://localhost:8000/login/",
  //       loginData
  //     ).then((res) => res.data);
  //     setUser(username);
  //     // console.log(user);
  //   } catch(err) {
  //     console.log("Login error", err);
  //   }
  // };

  const getKakaoAccessToken = async () => {
    try {
      const kakaoLoginData = await KakaoLogin.login()
        .then((res) => res.accessToken);
      signInWithAccessToken(kakaoLoginData);
    } catch(err) {
      console.error("Kakao login error", err);
    }
  }

  const signInWithAccessToken = async (accessToken: any) => {
    try {
      const username = await axios.post(
        "http://localhost:8000/login/",
        { "access_token": accessToken }
      ).then((res) => res.data);
      setUser(username);
    } catch (err) {
      console.error("Error signing in to server", err);
    }
  }

  return (
    <SafeAreaView>
      <Pressable onPress={() => getKakaoAccessToken()}>
        <Text>액세스 토큰</Text>
      </Pressable>
      <Text>{user}</Text>
    </SafeAreaView>
  )
}

export default App;
