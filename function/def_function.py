import librosa
import librosa.display
import soundfile as sf
import math


'''
def_function.py의 function 함수는 aaa.wav 파일을 bbb.wav로 바꿔준다

audio_path : 음원이 있는 위치(.wav 파일 불러오기)         /a/aa/aaa.wav
save_path : 처리된 음원을 저장할 위치(.wav로 저장해야함)  /b/bb/bbb.wav
start_time : 음원 시작 시간
end_time : 음원 끝 시간
target_bpm : 듣고 싶은 bpm

'''


def function(audio_path, save_path, start_time, end_time,target_bpm):
    #load music
    y, sr = librosa.load(audio_path, sr= 96000) # sampling rate은 나중에. 정할 수 있음
    tempo, beat_frames = librosa.beat.beat_track(y=y,sr=sr)

    # trim
    new_y = y[sr*start_time :sr*end_time]

    # speed
    rate = math.ceil(target_bpm/tempo) # 늘릴 노래 rate 계산
    y_fast = librosa.effects.time_stretch(new_y, rate=rate)

    # save file
    sf.write(save_path, y_fast, sr)