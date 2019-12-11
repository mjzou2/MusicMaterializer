import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fftpack import fft, fftfreq
import numpy as np
import argparse
from helper_functions import detect_onset
import finer_split as splt
import math
from music_analysis import audio_onset

def get_arguments():
    desc = "Converts sound to sheet music"
    parser = argparse.ArgumentParser(description = desc)
    parser.add_argument('wav_file', help='Input wav file', type=str)
    parser.add_argument("qpm", help='Input quarter notes per minute', type=int)
    return parser.parse_args()


def plot(wav):
    rate, samples = wavfile.read(wav)
    # samples = samples[:, 1]
    x = np.linspace(0.0, 17.0, num=len(samples))
    print(len(x))
    print(rate)

    #samples = samples / (convert_16_bit + 1.0)
    y = samples
    # z = samples[:, 1]
    # print(samples)
    plt.plot(x, y)
    # plt.plot(x, z)
    plt.show()


def trim_wav(original, onset_time):
    rate, samples = wavfile.read(original)
    if onset_time == -1:
        print(rate, len(samples))
        wavfile.write("trimmed.wav", rate, samples)
    print(len(samples) / rate)
    samples = samples[:math.floor(onset_time * rate)]
    wavfile.write("trimmed.wav", rate, samples)


def spectrum(wav_file, start, end):
    wav_file = wav_file[start: end]
    sqmags = []
    frequencies = []
    for wave in wav_file:
        rate, samples = wavfile.read(wave)
        samples = samples[:, 0]
        samples = [(ele / 2**16) for ele in samples]
        sample_count = len(samples)
        amplitude = fft(samples)
        amplitude = amplitude[: (sample_count // 2 - 1)]
        frequency = fftfreq(sample_count, 1 / rate)[: sample_count//2 - 1]
        sqmag = [(abs(e) ** 2) for e in amplitude]
        sqmags.append(sqmag)
        frequencies.append(frequency)
    return sqmags, frequencies


def plot_spectrum(amplitude, frequencies):
    fig, axs = plt.subplots(len(amplitude))
    fig.suptitle('consecutive discrete notes')
    for i in range(len(amplitude)):
        axs[i].plot(frequencies[i], amplitude[i])
    plt.show()

def get_peak(wav):
    rate, samples = wavfile.read(wav)
    if samples.ndim > 1:
        samples = [max(samples[i]) for i in range(rate)]

    slope = [(samples[i + 1] - samples[i]) for i in range(rate - 1)]
    peak_index = []
    for i in range(rate - 2):
        if slope[i] > 0 and slope[i + 1] < 0:
            peak_index.append(i + 1)

    peak = [samples[i] for i in peak_index]
    print(len(peak))
    peak = np.array(peak)
    peak = peak[peak >= 0]
    x = np.linspace(0.0, 17.0, num=len(peak))
    y = peak
    plt.plot(x, y)
    # plt.plot(x, z)
    plt.show()




if __name__ == "__main__":
    arg = get_arguments()
    wav = arg.wav_file
    qpm = arg.qpm
    plot(wav)
    get_peak(wav)
    # onsetTime = detect_onset.detect_onset(wav)
    # print("By threshold ", onsetTime)
    onsetTime = audio_onset(wav) / 1000
    print("Onset ", onsetTime)
    #trim_wav(wav, onsetTime)
    wav_files = splt.split(wav, qpm)
    amplitude, frequencies = spectrum(wav_files, 9, 15)
    plot_spectrum(amplitude, frequencies)