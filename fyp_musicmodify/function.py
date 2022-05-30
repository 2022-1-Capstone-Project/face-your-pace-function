import librosa
import librosa.display
import soundfile as sf
from pygame import mixer
import pygame

import math
import wave



import sounddevice as sd

def mp3_to_wav(audio):
    # ffmpeg 설치 안됨
    # sf.write(save_path1, ny, sr, 'PCM_24')
    
    # sound = pydub.AudioSegment.from_wav("D:/example/apple.wav")
    # sound.export("D:/example/apple.mp3", format="mp3")
    pass



def get_bpm(audio_file):
    y, sr = librosa.load(audio_file)
    #y_percussive = librosa.effects.hpss(y)
    tempo, beat_frames = librosa.beat.beat_track(y=y,sr=sr)
    #print('Tempo : {:.2f}'.format(tempo))
    return tempo

def trim_audio_data(audio_file, save_file, start_time, end_time): 
    # 인자에 start_time 이랑 end_time 넣음 됨
    # 오디오 length 이후의 값을 넣을 때는 오류처리..? 아니면 애초에 인자 받을 때 그런 처리를 해도 되긴 하고
   
    sr = 96000 # sample rate
    sec = 30

    y, sr = librosa.load(audio_file, sr=sr) # load

    #ny = y[sr*20 :sr*120] # 시작시간 20초, 끝나는 시간 120초
    ny = y[sr*start_time :sr*end_time]
    #librosa.output.write_wav(save_file + '.wav', ny, sr)
    #sf.write('stereo_file1.wav', reduced_noise, 48000, 'PCM_24')
    sf.write(save_file, ny, sr, 'PCM_24')

def playback_speed(audio_path, save_path, rate = 1):
    y, sr = librosa.load(audio_path)
    y_fast = librosa.effects.time_stretch(y, rate=rate)
    sf.write(save_path, y_fast,sr)

def playsong(audio_path, loop = 1):
    pygame.init()
    mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play(loop) 


if __name__ == '__main__':
    '''
    사용자 입력
    '''
    audio_path = 'ONLY YOUR STARS! (Trickstar ver.).wav'
    start_time = 0 # 노래 시작 시간
    end_time = 90 # 노래 끝 시간
    target_bpm = 180 # 듣고싶은 속도
    #loop=1 # 몇 번

    #load music, 음원 길이
    y, sr = librosa.load(audio_path) # sampling rate은 나중에. 정할 수 있음
    #print(len(y))
    length = round(len(y)/sr,2) # round 하든지(소수점반올림) math.floor 사용하던지(내림->그냥 정수)
    print(length)
    #print(len(y)/sr)
    #print(sr)
  

    #음원 길이
    # w = wave.open(audio_path)
    # wavLen = w.getnframes() / w.getframerate()
    # print(wavLen)


    # get bpm
    tempo, beat_frames = librosa.beat.beat_track(y=y,sr=sr)
    rate = math.ceil(target_bpm/tempo) # 늘릴 노래 rate
    print('tempo : {}, rate : {}'.format(tempo,rate))
    
    # trim
    new_y = y[sr*start_time :sr*end_time]

    # speed
    y_fast = librosa.effects.time_stretch(new_y, rate=rate)
    print(type(y_fast))
    print(1)
    #sd.play(y_fast) # ? 왜 play 안되는 것... 
    print(2)

    # save file
    save_path1 = audio_path[:-4] + '_done' + '.wav'
    sf.write(save_path1, y_fast, sr)






    # loop, play
    # pygame.init()
    # mixer.init()
    #pygame.mixer.music.load(audio_path)
    # save_path1 = 'test1_'+audio_path[:-4] + '.wav'
    # sf.write(save_path1, new_y, sr)



    # pygame.mixer.music.load(save_path1)
    # print(1)
    # pygame.mixer.music.play(loop) 
    # print(2)
    # save_path1 = 'test1_'+audio_path[:-4] + '.wav'
    # save_path2 = 'test2_'+audio_path[:-4] + '.wav'
    # # y, sr = librosa.load(audio_path)
    # print(save_path2)