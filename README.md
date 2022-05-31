# face-your-pace-function

# 1. fyp_download.py 
```
python fyp_download.py 'https://soundcloud.com/ferret-lie/only-your-stars-trickstar-ver' 'C:\Users\yoondain\Desktop\capstone'
```
python fyp_download.py 링크 저장할주소 형식으로 입력하면 된다.</br>
![image](https://user-images.githubusercontent.com/76734572/171096196-113e1b27-ec9a-4f94-a1d8-2112320b6fb1.png)
</br>
~~링크과 저장할 주소에 띄어쓰기가 있다면 따옴표('') 로 묶어야 한다. 그렇지 않으면 서로 다른 argv 로 인식한다.</br>~~
**무조건 '' 로 묶을 것! 사클 링크에 % $ # 등 특수기호가 있음. 이걸 ''로 묶지 않으면 인식을 못한다** </br>
약 2분 정도 소요된다</br>

## 역할
1. 노래 다운
2. 노래 제목, 재생 길이, 커버사진을 $ 를 구분자로 return 
```
# fyp_download.py 77번쨰 line 참조
return (title[6:]+'$'+length[7:-8]+'$'+image_xpath)
```
![image](https://user-images.githubusercontent.com/76734572/170977780-0617683d-31b0-444a-a6ab-fb9b7dd5bc5d.png)</br>
위처럼 return

## 코드
![image](https://user-images.githubusercontent.com/76734572/170977182-b0fd64d0-38ce-4525-af8f-d99f9c4d0a7a.png)
fyp_download.py 에서 chromedriver 옵션을 설정하는 부분이다.
- option : 16번째 line은 저장할 경로이니 건들면 안되고, 17~21은 알아서 조절하면 된다.
- driver : selenium의 버전이 4가 됨에 따라서 여는 방식이 달라졌다고 한다. 여기서 에러가 나면 executable_path = '~/~/~/chromedriver' 인자를 입력하면 된다 

----
# 2. fyp_musicmodify.py
```
python fyp_musicmodify.py 'The Tempest Night-full-.mp3'  'test5.wav' '00:20' '01:00' '100'    
```
python fyp_musicmodify.py mp3주소 저장할wav주소 시작시간 끝시간 원하는템포 형식으로 입력하면 된다 </br>
![image](https://user-images.githubusercontent.com/76734572/171096112-3e08b093-b0eb-4e2c-9f9a-853eac211fe3.png)</br>
sr ( sampling rate ) 에 따라 소요 시간이 다름. sr에 따라 tempo의 값이 조금씩 다름. sr = 96000 (96kHz) 일 때가 가장 이상적 </br>
최소 40초부터 최대 90초 소요</br>
## 역할
시작시간, 끝시간, 원하는 템포를 입력받아 그 wav파일을 만들어 저장한다.






























