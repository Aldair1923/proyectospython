#proyecto python2
import os
os.chdir('c:/Users/ALDAIR AGUIRRE/Desktop/PROYECTO GUITARRA PYTHON/')
import wave
import numpy as np
samplerate=44100

def get_wave(freq,duration=0.5):
    amplitude =4096
    t=np.linspace(0,duration,int(samplerate * duration))
    wave = amplitude * np.sin(2*np.pi*freq*t)
    return wave

from pprint import pprint
def get_piano_notes():
    octave = ['do','do#','re','re#','mi','fa','fa#','sol','sol#','la','la#','si',
              'do2','do#2','re2','re#2','mi2','fa2','fa#2','sol2','sol#2','la2','la#2','si2']
    base_freq=261.63
    note_freqs={octave[i]:base_freq * pow(2,(i/12)) for i in range(len(octave))}
    note_freqs['']=0.0
    return note_freqs

note_freqs=get_piano_notes()
pprint(note_freqs)

import numpy as np
def get_song_data(music_notes):
    note_freqs=get_piano_notes()
    song=[get_wave(note_freqs[note])for note in music_notes.split('-')]
    song=np.concatenate(song)
    return song

#music_notes='do-re-mi-fa-sol-fa-mi-re-do'
#music_notes='do-do-re-do-fa-mi-do-do-re-do-sol-fa-do-do-do2-la-fa-fa-mi-re-la#-la#-la-fa-sol-fa'
notas_cancion='re2-re2-re2-mi2-mi2-fa#2-re2-mi2-re2-re2-re2-mi2-mi2-fa#2-re2-mi2-do2-re2-do2-si-la-sol-fa#-re-si-do2-si-la-sol-fa#-mi-sol-fa#-mi-re#-la-sol-fa#-mi-si-do2-si-la-sol-re2-re2'
data=get_song_data(notas_cancion)

data=data * (16300/np.max(data))

from scipy.io.wavfile import write
write('micancion2b1x.wav',samplerate,data.astype(np.int16))
