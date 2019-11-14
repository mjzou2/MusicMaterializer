import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fftpack import fft, fftfreq
import numpy as np
import argparse
from helper_functions import detect_onset
import finer_split as splt
import math

def get_arguments():
    desc = "Converts sound to sheet music"
    parser = argparse.ArgumentParser(description = desc)
    parser.add_argument('wav_file', help='Input wav file', type=str)
    parser.add_argument("qpm", help='Input quarter notes per minute', type=int)
    return parser.parse_args()


def plot(wav):
    convert_16_bit = float(2 ** 15)
    rate, samples = wavfile.read(wav)
    # samples = samples[:, 1]
    x = np.linspace(0.0, 17.0, num=len(samples))
    print(len(x))
    print(rate)

    #samples = samples / (convert_16_bit + 1.0)
    y = samples[:, 0]
    z = samples[:, 1]
    # print(samples)
    plt.plot(x, y)
    plt.plot(x, z)
    plt.show()


def trim_wav(original, onset_time):
    if onset_time == -1:
        return
    rate, samples = wavfile.read(original)
    print(len(samples) / rate)
    samples = samples[math.floor(onset_time * rate):]
    wavfile.write("trimmed.wav", rate, samples)


def spectrum(wav_file):
    rate, samples = wavfile.read(wav_file[0])
    samples = samples[:, 0]
    samples = [(ele / 2**16) for ele in samples]
    sample_count = len(samples)
    amplitude = fft(samples)
    amplitude = abs(amplitude[: (sample_count // 2 - 1)])
    frequencies = fftfreq(sample_count, 1 / rate)[: sample_count//2 - 1]
    print(frequencies)
    print("Amplitude ", len(amplitude), " Frq ", len(frequencies))
    sqamp = [(e ** 2) for e in amplitude]

    fig, axs = plt.subplots(2)
    fig.suptitle("Og Vs. sq")
    axs[0].plot(amplitude, frequencies)
    axs[1].plot(sqamp, frequencies)
    plt.show()


if __name__ == "__main__":
    arg = get_arguments()
    wav = arg.wav_file
    qpm = arg.qpm
    # plot(wav)
    onsetTime = detect_onset.detect_onset(wav)
    print("By threshold ", onsetTime)
    trim_wav(wav, onsetTime)
    wav_files = splt.split("trimmed.wav", qpm)
    spectrum(wav_files)