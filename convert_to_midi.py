import midi


class ConvertToMidi:
    noteName = []
    bpm = []
    constVelocity = 30
    timeInt = 1

    # constructor
    def __init__(self, notes, tempo):
        print("constructing...")
        self.noteName = notes
        self.bpm = tempo

    # convert notes and output the midi file
    def toMidi(self):
        print("called toMidi")
        # create midi pattern and track
        pattern = midi.Pattern()
        track = midi.Track()
        pattern.append(track)

        print("start appending note events")
        for i in range(len(self.noteName)):
            for j in range(len(self.noteName[i])):
                on = midi.NoteOnEvent(tick = 0, velocity = self.constVelocity, pitch = self.noteName[i][j])
                track.append(on)
            
            for k in range(len(self.noteName[i])):
                off = midi.NoteOffEvent(tick = self.timeInt, velocity = self.constVelocity, pitch = self.noteName[i][j])

        print("creating eot...")
        eot = midi.EndOfTrackEvent(tick = 1)
        track.append(eot)

        print ("This is the pattern")
        print (pattern)

        print ("Saving ...")
        midi.write_midifile("output.mid", pattern)

