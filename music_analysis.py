from scipy.io import wavfile
from scipy.fftpack import fft,fftfreq
import numpy as np
from math import log2, pow

def loudest_freqs(wav_file):
    min_amp = 100_000_000 #i have no idea what this should be set to
    samplerate, data = wavfile.read(wav_file)
    samples = len(data)
    if data.ndim > 1: #if two (plus?) channels
        #data = [(data[i][0] + data[i][1]) / 2 for i in range(samples)] decide on taking avg or max of channels
        data = [max(data[i]) for i in range(samples)]
    abs_fft = np.abs(fft(data)[:samples//2])
    freqs = fftfreq(samples, 1/samplerate)[:samples//2] #only need positive first halves
    pitches_recorded = []
    louds = []
    for i in range(1, samples//2): #start at index 1 because heck 0 freq
        if abs_fft[i] > min_amp:
            p = pitch(freqs[i])
            if p not in pitches_recorded:
                pitches_recorded.append(p)
                louds.append(freqs[i])
    if louds == []:
        return None
    return louds

def analyse_wavs(wavs):
    freqs = []
    for wav in wavs:
        freqs.append(loudest_freqs(wav))
    return freqs

# https://www.johndcook.com/blog/2016/02/10/musical-pitch-notation/
def pitch(freq):
    A4 = 440
    C0 = A4*pow(2, -4.75)
    name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    h = round(12*log2(freq/C0))
    octave = h // 12
    n = h % 12
    return name[n] + str(octave)

