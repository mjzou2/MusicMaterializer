import pyaudio
import wave
import sys
import keyboard

chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "audio.wav" % (self.get('subject_nr'), self.get('count_inline_script'))

p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
		channels = CHANNELS,
		rate = RATE,
		input = True,
		frames_per_buffer = chunk)


print("Press R to start recording")
all=[]
while True:
    try:
	if keyboard.is_pressed('r'):
	    print("Recording...")
	    print("Press S to stop recording")
	    while True:
		data = stream.read(chunk)
		all.append(data)
		try:
		    if keyboard.is_pressed('s'):
			print("Recording stopped.")
			break
		    else:
			pass
	    break
	else:
	    pass
    except:
	# do nothing

# write data to WAVE file
data = ''.join(all)
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(data)
wf.close()
