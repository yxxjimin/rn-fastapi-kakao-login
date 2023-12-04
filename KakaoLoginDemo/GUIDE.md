## Getting Started
Refer to [@react-native-seoul/kakao-login](https://github.com/crossplatformkorea/react-native-kakao-login#getting-started) for more details.

### iOS
1. Register Platform

From [Kakao Developers console](https://developers.kakao.com/console/), register iOS platform and specify the bundle identifier.

2. Configure `Info.plist`

Add some settings to `Info.plist`. Note the differences in `<string>kakao{카카오 네이티브앱 키}</string>` and `<string>{카카오 네이티브앱 키}</string>`.

3. Create Swift Bridging Header

Create `SwiftBridge.swift` and edit `AppDelegate.mm`.

4. Install Pods

```bash
cd ios
pod install
```