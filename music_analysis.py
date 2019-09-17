from scipy.io import wavfile
from scipy.fftpack import fft,fftfreq
import numpy as np

def loudest_freq(wav_file): 
    samplerate, data = wavfile.read(wav_file)
    samples = len(data)
    abs_fft = np.abs(fft(data)[:samples//2])
    freqs = fftfreq(samples, 1/samplerate)[:samples//2] #only need positive first halves
    max_v = np.amax(abs_fft)
    max_i = np.where(abs_fft == max_v)[0]
    max_f = float(freqs[max_i])
    return max_f

