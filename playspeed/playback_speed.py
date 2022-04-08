from playsound import playsound
import librosa
import ffmpeg
import multiprocessing
#import vlc 
import time
import wave
import pydub
import wave
import os, sys
from pydub import AudioSegment
from pydub.playback import play


import soundfile as sf
import pyrubberband as pyrb

#wave
CHANNELS = 1
swidth = 2
Change_RATE = 2

def get_bpm(audio_path):
  #audio_path = 'dakara.wav'# BPM 105
  y, sr = librosa.load(audio_path)
  #y_percussive = librosa.effects.hpss(y)
  tempo, beat_frames = librosa.beat.beat_track(y=y,sr=sr)
  print('Tempo : {:.2f}'.format(tempo))

def speed_change(sound, speed=1.0):
    # Manually override the frame_rate. This tells the computer how many
    # samples to play per second
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
         "frame_rate": int(sound.frame_rate * speed)
      })
     # convert the sound with altered frame rate to a standard frame rate
     # so that regular playback programs will work right. They often only
     # know how to play audio at standard frame rate (like 44.1k)
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

if __name__ == '__main__':
  # liborsa - get bpm
  #audio_path = sys.argv[1]
  #get_bpm(audio_path)

  #wave
  # spf = wave.open('test.wav', 'rb')
  # RATE=spf.getframerate()
  # signal = spf.readframes(-1)

  # wf = wave.open('changed.wav', 'wb')
  # wf.setnchannels(CHANNELS)
  # wf.setsampwidth(swidth)
  # wf.setframerate(RATE*Change_RATE)
  # wf.writeframes(signal)
  # wf.close()


  #pydub
  # song = AudioSegment.from_wav("dakara.wav") 
  # #song = AudioSegment.from_mp3("dakara.mp3") #mp3 - ffmpeg 에서 무슨 오류
  # slow_sound = speed_change(song, 0.75)
  # fast_sound = speed_change(song, 2.0)
  # play(slow_sound)

  sound = AudioSegment.from_wav("dakara.wav")
  #sound = AudioSegment.from_mp3(sys.argv[1])
  #sound.export("file.wav", format="wav")

  #print(sys.argv[1])

  y, sr = sf.read("dakara.wav")
  # Play back at extra low speed
  y_stretch = pyrb.time_stretch(y, sr, 0.5)
  # Play back extra low tones
  y_shift = pyrb.pitch_shift(y, sr, 0.5)
  sf.write("analyzed_filepathX5.wav", y_stretch, sr, format='wav')

  sound = AudioSegment.from_wav("analyzed_filepathX5.wav")
  play(sound)





  sound.export("analyzed_filepathX5.mp3", format="mp3")

  # Play back at low speed
  y_stretch = pyrb.time_stretch(y, sr, 0.75)
  # Play back at low tones
  y_shift = pyrb.pitch_shift(y, sr, 0.75)
  sf.write("analyzed_filepathX75.wav", y_stretch, sr, format='wav')

  sound = AudioSegment.from_wav("analyzed_filepathX75.wav")
  sound.export("analyzed_filepathX75.mp3", format="mp3")

  # Play back at 1.5X speed
  y_stretch = pyrb.time_stretch(y, sr, 1.5)
  # Play back two 1.5x tones
  y_shift = pyrb.pitch_shift(y, sr, 1.5)
  sf.write("analyzed_filepathX105.wav", y_stretch, sr, format='wav')

  sound = AudioSegment.from_wav("analyzed_filepathX105.wav")
  sound.export("analyzed_filepathX105.mp3", format="mp3")

  # Play back at same speed
  y_stretch = pyrb.time_stretch(y, sr, 1)
  # Play back two smae-tones
  y_shift = pyrb.pitch_shift(y, sr, 1)
  sf.write("analyzed_filepathXnormal.wav", y_stretch, sr, format='wav')

  sound = AudioSegment.from_wav("analyzed_filepathXnormal.wav")
  sound.export("analyzed_filepathXnormal.mp3", format="mp3")
