# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView

from .forms import FileForm
from .models import FileModel


def home(request):
    return render(request, 'home.html')


def upload(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES, request.POST)
        if form.is_valid():

            formNew = convert(form)

            formNew.save()
            return redirect('file_list')	
    else:
        form = FileForm()
        
    return render(request, 'upload_file.html', {
        'form': form
    })


def delete_file(request, pk):
    if request.method == 'POST':
        file_delete = FileModel.objects.get(pk=pk)
        file_delete.delete()
    return redirect('file_list')


def file_list(request):
    files = FileModel.objects.all()
    return render(request, 'file_list.html', {
        'files': files   
    })


def help(request):
    return render(request, 'help.html')





import wave, array, math, time, argparse, sys
from scipy.io import wavfile
from scipy.fftpack import fft, fftfreq
import midi
import pydub
import os
import errno
import subprocess
import math
import numpy as np
from helper_functions import convert_to_midi, export


def get_arguments():
    desc = "Converts sound to sheet music"
    parser = argparse.ArgumentParser(description = desc)
    parser.add_argument('wav_file', help='Input wav file', type=str)
    parser.add_argument('bpm', help='bpm of music', type=int)
    parser.add_argument('export', help='export file name', type = str)

    return parser.parse_args()


def pitch(freq):
    A4 = 440
    C0 = A4*pow(2, -4.75)
    name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    h = round(12*math.log2(freq/C0))
    octave = h // 12
    n = h % 12
    return name[n] + str(octave)


def loudest_freqs(wav_file):
    """
    Finds loudest frequencies given wav.

    Parameters:
        wav_file: a string contating the name of an accessible wav file

    Returns:
        None if no frequency above specified loudness (min_amp),
        othwerise returns list of unique frequencies as floats.
    """

    min_amp = 10000000
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
            if freqs[i] < 27.5:
                continue
            p = pitch(freqs[i])
            if p not in pitches_recorded:
                if len(louds) != 0:
                    if math.ceil(math.log2(round(freqs[i] / louds[0]))) == math.floor(math.log2(round(freqs[i] / louds[0]))):
                        continue
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

def split(wav, tempo):
    wav_seg = pydub.AudioSegment.from_file(wav, "wav")
    chunk_length = (60 / tempo) * 1000
    chunks = pydub.utils.make_chunks(wav_seg, chunk_length)
    #dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = os.getcwd()
    filenames = []
    for i, chunk in enumerate(chunks):
        chunk_name = "/temp/chunk%s.wav" % i
        full_chunk_path = dir_path + chunk_name
        filenames.append(full_chunk_path)
        os.makedirs(os.path.dirname(full_chunk_path), exist_ok=True)
        with open(full_chunk_path, "wb") as f:
            chunk.export(f, format = "wav")
    return len(chunks), filenames


def convert(inputFile):    
    #args = get_arguments()
    bpm = inputFile.apikey # find a way to have user input bpm
    input = inputFile.file
    output = FileForm(inputFile.title, inputFile.file + '.mid', inputFile.apikey, inputFile.detect_bpm, inputFile.record) 
    num_of_chunks, wavs = split(input, bpm)
    # wavs = ["/temp/chunk%s.wav" % i for i in range(num_of_chunks)]
    freqs = analyse_wavs(wavs)
    converter = convert_to_midi.ConvertToMidi(freqs, bpm, output)
    converter.toMidi()
    export.export_to_pdf(output + '.mid')
    return output
    #export.export_to_flat(output, output + '.mid')

