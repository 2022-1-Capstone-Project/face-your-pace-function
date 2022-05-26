# 1. selenium, pyperclip 라이브러리 설치 
명령 프롬포트에 다음과 같은 명령어 입력
## windows
```
pip install selenium
pip install pyperclip
```
## mac
```
pip3 install selenium
pip3 install pyperclip
```

# 2. 크롬 드라이버 설치
크롬 브라우저 버전 확인 </br>
https://mainia.tistory.com/2616

## windows
버전과 동일한 exe 다운 https://chromedriver.chromium.org/downloads </br>
https://chancoding.tistory.com/136 참고함
```
from selenium import webdriver

# windows Chrome
driver = webdriver.Chrome(executable_path='경로/chromedriver.exe')
```
chrome.exe 를 실행하려는 .py 파일과 같은 폴더에 넣고 
```
driver = webdriver.Chrome()
```
로도 열 수 있다.


## mac
mac에서는 위에서 mac 버전의 chromedriver를 사용하셔도 되고 brew에서 chromedriver을 설치해도 된다. </br>
여기서는 brew를 사용하도록 하겠다. 명령 프롬포트에 다음의 명령어를 입력한다.
```
brew install chormedriver
```

```
from selenium import webdriver

# mac Chrome (brew로 chromedriver 설치한 경우)
driver = webdriver.Chrome()

# mac Chrome - exe로 설치한 경우
driver = webdriver.Chrome("chrome webdriver 저장 위치")
```
mac 환경에서는 brew와 pip 사용을 권장합니다 </br>
https://blog.naver.com/lynn1128/222310925258


# 3. 사운드클라우드 링크, 다운받을 경로 입력 
face-your-pace-function/download/test.py 의 6번째와 7번째 line을 수정하면 된다. </br>
mp3 로 다운받고 싶다면 6번째 line만 실행, wav로 다운받고 싶다면 7번째 line만 실행
![image](https://user-images.githubusercontent.com/76734572/170465435-6fd54e5e-51c3-4e0a-a086-c143f5058c21.png)
