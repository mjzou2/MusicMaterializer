import wave, array, math, time, argparse, sys
from scipy.io import wavfile
from scipy.fftpack import fft, fftfreq
import midi

def loudest_freqs(wav_file):
    """
    Finds loudest frequencies given wav.
    
    Parameters:
        wav_file: a string contating the name of an accessible wav file
    
    Returns:
        None if no frequency above specified loudness (min_amp),
        othwerise returns list of unique frequencies as floats.
    """

    min_amp = 100000000
    samplerate, data = wavfile.read(wav_file)
    samples = len(data)
    if data.ndim > 1:
        data = [max(data[i]) for i in range(samples)]
    abs_fft = np.abs(fft(data)[:samples//2])
    freqs = fftfreq(samples, 1/samplerate)[:samples//2]
    pitches_recorded = []
    louds = []
    for i in range(1, samples//2):
        if abs_fft[i] > min_amp:
            p = pitch(freqs[i])
            if p not in pitches_recorded:
                pitches_recorded.append(p)
                louds.append(freqs[i])
    if not louds:
        return None
    return louds
    

def analyse_wavs(wavs):
    """
    Takes in list of names of wav files and returns 2D list of loudest_freqs output. 
    See documentation of loudest_freqs for more info.
    """
    return [loudest_freqs(wav) for wav in wavs]

    
def freq_to_str(freq):
    """
    Takes in numeric frequency and returns name of respective note. 
    Returns only sharp equivalent of non-natural notes.
    """
    A4 = 440
    C0 = 440*math.pow(2, -4.75)
    name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    h = round(12*math.log2(freq/C0))
    octave = h // 12
    n = h % 12
    return name[n] + str(octave)
    
    


