import pydub
import os
import errno

def split(wav, tempo):
    wav_seg = pydub.AudioSegment.from_file(wav, "wav")
    chunk_length = (60 / tempo) * 1000
    chunks = pydub.utils.make_chunks(wav_seg, chunk_length)
    for i, chunk in enumerate(chunks):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        chunk_name = "/temp/chunk%s.wav" % i
        full_chunk_path = dir_path + chunk_name
        os.makedirs(os.path.dirname(full_chunk_path), exist_ok=True)
        with open(full_chunk_path, "wb") as f:
            chunk.export(f, format = "wav")


