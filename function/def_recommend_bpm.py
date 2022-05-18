import math
def rec_bpm(age, height, target_pace, stride):
    age = int(age)
    height = int(height)
    target_pace = int(target_pace)
    stride = int(stride)


    # kilo_per_hour = 3600/target_pace   # km/h
    footnum = math.ceil(100000/stride) # 보폭으로 뛰었을 때 몇번 발걸음을 해야하는지


    recommend_bpm = footnum/(target_pace/60)
    bpm1 = math.trunc(recommend_bpm)
    print(bpm1)
    #bpm2 = bpm1

    if (bpm1 % 10 >0 or bpm1%10==0 ) and bpm1%10<5:
        bpm1 = round(bpm1,-1)
        # bpm2 = bpm1 - bpm1%10 + 5
    else:
        # bpm2 = round(bpm1,-1)
        bpm1 = bpm1 - bpm1%10 + 5

    # print('rec bpm = {} ~ {}'.format(bpm1,bpm2))
    return str(bpm1)
