import sys
def rec_bpm(age, height, workout_level, target_pace, stride):
    age = int(age)
    height = int(height)
    workout_level=workout_level
    target_pace = int(target_pace) # 이것도 '00:00' 꼴로? 
    stride = int(stride)

    if target_pace != 0 and stride == 0: # 타겟 페이스는 있는데 보폭을 모를 때

        a = height * 0.37
        b = height - 100
        c = height * 0.45

        if a > c and c >= b : 
            max_stride = a
            min_stride = b

        elif a > b and b >= c : 
            max_stride = a
            min_stride = c

        elif b > c and c >= a : 
            max_stride = b
            min_stride = a

        elif b > a and a >= c : 
            max_stride = b
            min_stride = c
            
        elif c > b and b >= a : 
            max_stride = c
            min_stride = a

        elif c > a and a >= b : 
            max_stride = c
            min_stride = b


        # print(stride) # 평균 보폭
        #stride = int(round((min_stride + max_stride)/2,-1))
        stride = round((min_stride + max_stride)/2)

    elif target_pace == 0 and stride != 0: # 타겟 페이스모름 보폭을 알 때 --> workout level로 파악
        if workout_level   == '1' : target_pace = 900  # 4km/h
        elif workout_level == '2' : target_pace = 600  # 6km/h
        elif workout_level == '3' : target_pace = 450  # 8km/h
        elif workout_level == '4' : target_pace = 360  # 10km/h
        elif workout_level == '5' : target_pace = 300  # 12km/h

    else: pass

    # kilo_per_hour = 3600/target_pace   # km/h
    footnum = int(100000/stride)+1 # 보폭으로 뛰었을 때 몇번 발걸음을 해야하는지


    recommend_bpm = footnum/(target_pace/60)
    bpm1 = int(recommend_bpm)
    print(bpm1)
    #bpm2 = bpm1
    return f'rec bpm = {bpm1} ~ {bpm1+5}'


    # 5 단위 굳이...? 
    if (bpm1 % 10 >0 or bpm1%10==0 ) and bpm1%10<5:
        bpm1 = round(bpm1,-1)
        # bpm2 = bpm1 - bpm1%10 + 5
    else:
        # bpm2 = round(bpm1,-1)
        bpm1 = bpm1 - bpm1%10 + 5

    # print('rec bpm = {} ~ {}'.format(bpm1,bpm2))
    # print('rec bpm = {} ~ {}'.format(bpm1,bpm1+5))
    return f'rec bpm = {bpm1} ~ {bpm1+5}'


if __name__ == '__main__':
    age = sys.argv[1]
    height = sys.argv[2]
    workout_level = sys.argv[3]
    target_pace = sys.argv[4]
    stride = sys.argv[5]
    rec_bpm(age, height, workout_level, target_pace, stride)
    # rec_bpm(age = '23', height='165',workout_level='고강도',target_pace='300',stride='0')
    pass