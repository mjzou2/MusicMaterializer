from scipy.io import wavfile
from scipy.fftpack import fft,fftfreq
import numpy as np
from math import log2, pow
import librosa

def loudest_freqs(wav_file):
    min_amp = 100000000 #i have no idea what this should be set to
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
        if abs_fft[i] == max(abs_fft):
            p = pitch(freqs[i])
            if p not in pitches_recorded:
                pitches_recorded.append(p)
                louds.append(freqs[i])
    if not loud:
        return None
    return louds

def analyse_wavs(wavs):
    return [loudest_freqs(wav) for wav in wavs]

# https://www.johndcook.com/blog/2016/02/10/musical-pitch-notation/
def pitch(freq):
    A4 = 440
    C0 = A4*pow(2, -4.75)
    name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    h = round(12*log2(freq/C0))
    octave = h // 12
    n = h % 12
    return name[n] + str(octave)

# audio wav onset detection
# https://musicinformationretrieval.com/onset_detection.html
def audio_onset(wav_file):
    x, sr = librosa.load(wav_file)
    onset_frames = librosa.onset.onset_detect(x, sr=sr, wait=1, pre_avg=1, post_avg=1,
            pre_max=1, post_max=1)
    onset_times = librosa.frames_to_time(onset_frames)
    onset_milliseconds = [i * 1000 for i in onset_times]
    print(onset_times)
    return onset_milliseconds[0], onset_times
