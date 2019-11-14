from scipy.io import wavfile

def detect_onset(wav):
    rate, data = wavfile.read(wav)
    if data.ndim > 1: #if two (plus?) channels
        data = [max(data[i]) for i in range(len(data))]
    min_amp = 10000 #seems okay?
    for i, sample in enumerate(data):
        if abs(sample) > min_amp:
            return i / rate
    return -1

