import midi

class toMidi(notes, tempo):
    out = midi.Pattern()
    notes.append(midi.EndOfTrackEvent(tick = 1))
    out.append(notes)
    midi.write_midifile("output.mid",out)
    
    
