
import math
if __name__ == '__main__':


    age = 23 # 이건 무조건 입력해야함!!

    '''
    case 1) 사용자가 입력을 다 했을 때
    '''
    # 사용자입력  
    target_pace = 450 # seconds 타겟 시간
    stride = 80 # centimeters 보폭
    # ==============================

    kilo_per_hour = 3600/target_pace # km/h
    footnum = math.ceil(100000/stride) # 보폭으로 뛰었을 때 몇번 발걸음을 해야하는지


    recommend_bpm = footnum/(target_pace/60)
    bpm1 = math.trunc(recommend_bpm)
    print(bpm1)
    bpm2 = bpm1

    if (bpm1 % 10 >0 or bpm1%10==0 ) and bpm1%10<5:
        bpm1 = round(bpm1,-1)
        bpm2 = bpm1 - bpm1%10 + 5
    else:
        bpm2 = round(bpm1,-1)
        bpm1 = bpm1 - bpm1%10 + 5

    print('rec bpm = {} ~ {}'.format(bpm1,bpm2))
    #print(recommend_bpm)




    '''
    case 2) 사용자가 자신의 페이스 등 모를 때
    '''
    workout_level = '저강도' # 초급. 중급. 고급 or 저강도, 중강도, 고강도 선택하게 --> 추천 용도..? 


    
    '''
    저강도; 최대심박수의 64%미만, 중강도; 
    최대심박수 64%-76%, 고강도; 
    최대심박 76%이상 
    예를 들어 45세 성인이 효과적인 운동을 하기 위해서는 최소 110박이상 맥박이 증가하고, 135박을 넘지 않도록 운동하면 적합한 운동입니다
    '''

    max_heartrate = 220-age # 최대심박수
    if workout_level == '저강도': max_heartrate*= .64
    elif workout_level == '중강도' : max_heartrate *= .76
