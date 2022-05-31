from hashlib import sha3_256
import librosa
import librosa.display
import soundfile as sf

from pydub import AudioSegment
import sys
import time

def to_sec(t):
    min, sec = t.rstrip().split(sep=":")
    return 60 * int(min) + int(sec)

def function(audio_path:str, save_path:str, start_time:str, end_time:str,target_bpm:str):
    start_time = to_sec(start_time) 
    end_time = to_sec(end_time)
    target_bpm = int(target_bpm)

    '''
    convert mp3 to wav  --> 약 1초 
    '''
    mp3_src = audio_path # "transcript.mp3"
    temp_wav_dst = mp3_src.rstrip().split(sep="/")[-1][:-4] + '.wav'  #"test.wav"       
    s1 = time.time()                                                     
    sound = AudioSegment.from_mp3(mp3_src)
    sound.export(temp_wav_dst, format="wav")
    s2 = time.time()   
    print(s2-s1) # 


    '''
    load wav file music --> 시간 제일 오래 걸림 아예 처음부터 다운받을 때 이 정보까지 추출해서 저장할까...?
    '''
    y, sr = librosa.load(temp_wav_dst,sr = 96000) # sampling rate은 나중에. 정할 수 있음
    print(f'sr : {sr}')
    # 96000 으로 할 때가 가장 정확.
    # prob : 100 이하가 나올 때. 
    # 
    # ex) 현재 only your star 이게 93 나오는데 다른 곳에서는 186으로 나옴
    # 만약 그렇게 되면 사용자가 input 을 120으로 넣게 되면 93으로 인식하면 빠르게 되고,
    # 186으로 인식하게 되면 느리게 될 것임

    s7 = time.time()
    print(s7-s2)

    '''
    temp 추출.librosa 로 load를 하고 추출 가능. sr = 96000으로 할 때 정확도가 가장 높음
    '''
    tempo, beat_frames = librosa.beat.beat_track(y=y,sr=sr) # sr낮게 해도 매우 가능
    # sr을 default로 하면 5초
    # sr 1000
    # sr 10000
    print(f'tempo  : {tempo}')
    s3 = time.time()
    print(s3-s7)
    
    
    '''
    시간 맞춰 trim
    '''
    # trim
    new_y = y[sr*start_time :sr*end_time]
    s4 = time.time()
    
    
    
    # speed
    rate = round(target_bpm/round(tempo),2) # 늘릴 노래 rate 계산 tempo는 소수점 첫째자리에서 반올림
    y_fast = librosa.effects.time_stretch(new_y, rate=rate)
    s5 = time.time()
    print(s5-s4)
    # save file
    sf.write(save_path, y_fast, sr)  # sr 높을 수록 시간 오래...
    s6 = time.time()
    print(s6-s5)

if __name__ == '__main__':
    # start = time.time()
    
    # end = time.time()
    # print('\n')
    # print(end-start)


    '''
    입력 형식
    function('The Tempest Night-full-.mp3', 'test5.wav','00:20','01:00','100')
    '''
    audio_path = sys.argv[1]  # mp3 file 위치, type:str
    save_path = sys.argv[2]  # modify 한 wav를 저장할 위치, type:str
    start_time = sys.argv[3] # '00:00' 형태, type:str
    end_time = sys.argv[4] # '00:00' 형태, type:str
    target_bpm = sys.argv[5] # '000' 형태, type:str
   
    function(audio_path, save_path, start_time, end_time,target_bpm)