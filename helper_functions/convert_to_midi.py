import midi
import audiolazy
from audiolazy import lazy_midi

# convert frequencies into Midi numbers
def frequencyToNote(frequencies):
    temp_list = []
    for i in range(len(frequencies)):
        temp = int(lazy_midi.freq2midi(frequencies[i]))
        if 0 <= temp <= 255:
            temp_list.append(temp)



    return temp_list


# convert the list of Midi numbers into a functional midi file
class ConvertToMidi:
    noteName = []
    bpm = []
    constVelocity = 30
    resolution = 240

    # constructor
    def __init__(self, notes, tempo, export):
        print("constructing...")
       
        self.noteName = notes
        for i in range(len(self.noteName)):
            if self.noteName[i] is None:
                self.noteName[i] = []
            for j in range(len(self.noteName[i])):
                self.noteName[i][j] = int(self.noteName[i][j])
            self.noteName[i] = frequencyToNote(self.noteName[i])
        self.export = export
        self.bpm = tempo
        print(self.noteName)

    # convert notes and output the midi file
    def toMidi(self):
        print("called toMidi")
        
        # create midi pattern and track
        pattern = midi.Pattern()
        track = midi.Track()
        pattern.append(track)

        # append note events to the track
        print("start appending note events")
        for i in range(len(self.noteName)):
            for j in range(len(self.noteName[i])):
                on = midi.NoteOnEvent(tick = 0, velocity = self.constVelocity, pitch = self.noteName[i][j])
                track.append(on)

            for k in range(len(self.noteName[i])):
                if k == 0:
                    off = midi.NoteOffEvent(tick = self.resolution, pitch = self.noteName[i][k])
                else:
                    off = midi.NoteOffEvent(tick = 0, pitch = self.noteName[i][k])
                track.append(off)

        # create eot
        print("creating eot...")
        eot = midi.EndOfTrackEvent(tick = 1)
        track.append(eot)

        print ("This is the pattern")
        print (pattern)
        
        # save the pattern to ./output.mid
        print ("Saving ...")
        midi.write_midifile(self.export, pattern)

        print ("Conversion finished")

"""
print ("running test")


notes = [[31, 57], [69], [48, 38]]
print (notes)

print(frequencyToNote([[440,220],[329.628,493.883]]))
test = ConvertToMidi(frequencyToNote([[440,220],[329.628,493.883]]), 90)
test.toMidi()

print("Test finished")
"""
