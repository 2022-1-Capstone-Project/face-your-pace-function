# face-your-pace-function

# 1. fyp_download.py 
```
python fyp_download.py https://soundcloud.com/ferret-lie/only-your-stars-trickstar-ver C:\Users\yoondain\Desktop\capstone
```
python fyp_download.py 링크 저장할주소 형식으로 입력하면 된다.</br>
링크과 저장할 주소에 띄어쓰기가 있다면 따옴표('') 로 묶어야 한다. 그렇지 않으면 서로 다른 argv 로 인식한다.</br>
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
