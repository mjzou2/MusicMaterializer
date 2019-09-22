# Andrew Tian

# create a function that receives a frequency and possibly tick value that returns
# a note in a MIDI track with an EndOfTrackEvent

# pseudocode
# function frequencyToNote(freqValue, tickValue, possibly loudness value too) 
# create temporary track
# create NoteOnEvent and NoteOffEvent(with default loudness if not specified)
# add both to temporary track
# add an EndOfTrackEvent to the temp track
# return the track

# notes
# NoteOnEvent - captures beginning of a note, tick is when event occurs, pitch is 
# frequency, velocity is how hard the key was pressed
# NoteOffEvent - captures end of a note, pitch is the note released(most likely same 
# value as NoteOnEvent), velocity is zero
# EndOfTrackEvent - special event that indicates to MIDI the end of a track, has tick 
# value of 1

import mido

def frequencyToNote(tickValue, loudnessValue, freqValue) :
	print("this function is run")
	track = midi.Track()
	on = midi.NoteOnEvent(0, loudnessValue, freqValue)
	off = midi.NoteOffEvent(tickValue, 0, freqValue)
	end = midi.EndOfTrackEvent()
	track.append(on)
	track.append(off)
	track.append(end)


frequencyToNote(120, 10, 10)
