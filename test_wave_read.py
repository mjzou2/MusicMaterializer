import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np
import argparse
from helper_functions import detect_onset


def get_arguments():
    desc = "Converts sound to sheet music"
    parser = argparse.ArgumentParser(description = desc)
    parser.add_argument('wav_file', help='Input wav file', type=str)
    return parser.parse_args()


def plot(wav):
    convert_16_bit = float(2 ** 15)
    sr, samples = wavfile.read(wav)
    samples = samples[:, 1]
    x = np.linspace(0.0, 17.0, num=len(samples))
    print(len(x))
    print(sr)

    #samples = samples / (convert_16_bit + 1.0)
    y = samples
    print(samples)
    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    arg = get_arguments()
    wav = arg.wav_file
    plot(wav)
    onsetTime = detect_onset.detect_onset(wav)
    print(onsetTime)
