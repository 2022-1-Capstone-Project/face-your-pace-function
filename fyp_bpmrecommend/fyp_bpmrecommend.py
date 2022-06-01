import sys

def to_sec(t):
    min, sec = t.rstrip().split(sep=":")
    return 60 * int(min) + int(sec)

def getStride(height : int):
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


        # 평균 보폭
    return round((min_stride + max_stride)/2)

def getTargetPace(age:int,workout_level:str):
    if age <= 30:
        if workout_level   == '1' : target_pace = 900  # 4km/h
        elif workout_level == '2' : target_pace = 600  # 6km/h
        elif workout_level == '3' : target_pace = 450  # 8km/h
        elif workout_level == '4' : target_pace = 360  # 10km/h
        elif workout_level == '5' : target_pace = 300  # 12km/h


    elif age > 30 and age <= 40:
        if workout_level   == '1' : target_pace = 900  # 4km/h
        elif workout_level == '2' : target_pace = 720  # 5km/h
        elif workout_level == '3' : target_pace = 600  # 6km/h
        elif workout_level == '4' : target_pace = 450  # 8km/h
        elif workout_level == '5' : target_pace = 360  # 10km/h

    elif age > 40 and age <= 50:
        if workout_level   == '1' : target_pace = 1800  # 2km/h
        elif workout_level == '2' : target_pace = 900  # 4km/h
        elif workout_level == '3' : target_pace = 720  # 5km/h
        elif workout_level == '4' : target_pace = 600  # 6km/h
        elif workout_level == '5' : target_pace = 450  # 8km/h

    return target_pace

def rec_bpm(age, height, workout_level, target_pace, stride):
    age = int(age)
    height = int(height)
    workout_level=workout_level
    target_pace = to_sec(target_pace) # 이것도 '00:00' 꼴로? 
    stride = int(stride)

    if target_pace != 0 and stride == 0: # 타겟 페이스는 있는데 보폭을 모를 때
        stride = getStride(height)

    elif target_pace == 0 and stride != 0: # 타겟 페이스모름 보폭을 알 때
        target_pace = getTargetPace(age,workout_level)

    elif target_pace == 0 and stride == 0: # 둘 다 모를 때
        stride = getStride(height)
        target_pace = getTargetPace(age,workout_level)
    else: pass # 둘 다 알 때


    # kilo_per_hour = 3600/target_pace   # km/h
    footnum = int(100000/stride)+1 # 보폭으로 뛰었을 때 몇번 발걸음을 해야하는지


    recommend_bpm = footnum/(target_pace/60)
    bpm = int(recommend_bpm)
    print(f'rec bpm = {bpm-5} ~ {bpm+5}')
    #bpm2 = bpm1
    return f'rec bpm = {bpm-5} ~ {bpm+5}'



if __name__ == '__main__':


    age = sys.argv[1] # 나이 , type:str
    height = sys.argv[2] # 키 , type:str
    workout_level = sys.argv[3] # 운동 강도 1~5 숫자가 클수록 고강도 , type:str
    target_pace = sys.argv[4] # '00:00' 형태. 타켓 페이스 , type:str
    stride = sys.argv[5] # 보폭  , type:str

    rec_bpm(age, height, workout_level, target_pace, stride)


    # rec_bpm(age = '23', height='165',workout_level='5',target_pace='00:00',stride='100')