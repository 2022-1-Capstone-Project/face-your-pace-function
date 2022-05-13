
import math
if __name__ == '__main__':

    # 이건 무조건 입력해야하는 정보
    age = 23 
    height = 165

   
    # case 1) 사용자가 입력을 다 했을 때
    # 사용자입력  
    target_pace = 360   # seconds 타겟 시간
    stride = 110         # centimeters 보폭
    # ==============================

    # case 2) 사용자가 자신의 페이스 등 모를 때
    '''
    아는 정보 : 나이, 키
    나이는 젊을 수록 많이 뛸 수 있다
    키는 클수록 보폭은 넓어진다

    저강도; 최대심박수의 64%미만, 중강도; 
    최대심박수 64%-76%, 고강도; 
    최대심박 76%이상 
    예를 들어 45세 성인이 효과적인 운동을 하기 위해서는 최소 110박이상 맥박이 증가하고, 135박을 넘지 않도록 운동하면 적합한 운동입니다

    사람들 보통 걷는 속도
    4km/h

    빠른 걸음
    6km/h

    가볍게 뛰기 
    8km/h

    아주 빨리 뛰기
    10km/h


    키에 따른 적정 보폭
    [키×0.45, 키×0.37, 키-100] 총 3회 계산한 후 최소 값과 최대값의 범위를 적정 보폭 범위로 정한다.


    '''

    # Karvonen 공식을 이용한 목표심박수(Target HR) 이용. 한국에서 가장 많이 사용되고 있기 때문.
    max_heartrate = 220-age # 최대심박수

    workout_level = '저강도' # 걷기, 저강도, 중강도, 고강도 선택 가능하게
   
    # 걷기   : 4  km/h
    # 저강도 : 6  km/h
    # 중강도 : 8  km/h
    # 고강도 : 10 km/h

    min_stride = height * 0.37
    max_stride = height - 100
    if height * 0.45 > max_stride:
        max_stride = height * 0.45
    
    stride = int(round((min_stride + max_stride)/2,-1))
    print(stride) # 평균 보폭

    if workout_level == '걷기' : target_pace = 900
    elif workout_level =='저강도': target_pace = 600    # 6km/h
    elif workout_level == '중강도' : target_pace = 450  # 8km/h
    elif workout_level == '고강도' : target_pace = 360  # 10km/h




    # 계산 =============================================================
    kilo_per_hour = 3600/target_pace   # km/h
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
    # Karvonen 공식을 이용한 목표심박수(Target HR) 이용. 한국에서 가장 많이 사용되고 있기 때문.
    max_heartrate = 220-age # 최대심박수

    workout_level = '저강도' # 걷기, 저강도, 중강도, 고강도 선택하게 --> 추천 용도..? 
    # if workout_level == '저강도': max_heartrate*= .64
    # elif workout_level == '중강도' : max_heartrate *= .76

    # 저강도 : 6  km/h
    # 중강도 : 8  km/h
    # 고강도 : 10 km/h
    min_stride = height * 0.37
    max_stride = height - 100
    if height * 0.45 > max_stride:
        max_stride = height * 0.45
    
    mean_stride = int(round((min_stride + max_stride)/2,-1))
    print(mean_stride) # 평균 보폭

    if workout_level == '걷기' : target_pace = 900
    elif workout_level =='저강도': target_pace = 600      # 6km/h
    elif workout_level == '중강도' : target_pace = 450  # 8km/h
    elif workout_level == '고강도' : target_pace = 360  # 10lm/h

    kilo_per_hour = 3600/target_pace   # km/h
    footnum = math.ceil(100000/mean_stride) # 보폭으로 뛰었을 때 몇번 발걸음을 해야하는지


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
    '''
    