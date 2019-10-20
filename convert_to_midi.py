import midi
from audiolazy import freq2midi, freq2str, str2freq

# convert frequencies into Midi numbers
def frequencyToNote(frequencies):
    tempList = frequencies.copy()
	
    for i in range(len(frequencies)):
        if frequencies[i] == None:
            tempList[i] = []
        else:
            tempList[i] = freq2midi(frequencies[i])
    
    print(tempList)
    return tempList

# convert the list of Midi numbers into a functional midi file
class ConvertToMidi:
    noteName = []
    bpm = 120
    constVelocity = 30
    resolution = 220

    # constructor
    def __init__(self, notes, tempo):
        print("constructing...")
        
        self.noteName = frequencyToNote(notes)
        
        for i in range(len(self.noteName)):
            for j in range (len(self.noteName[i])):
               self.noteName[i][j] = round(self.noteName[i][j])
        
        self.bpm = tempo
      
    # convert notes and output the midi file
    def toMidi(self):
        print("called toMidi")
        print(self.noteName)
        # create midi pattern and track
        pattern = midi.Pattern()
        track = midi.Track()
        pattern.append(track)
        
        # append note events to the track
        print("start appending note events")
        tempo = midi.SetTempoEvent()
        tempo.set_bpm(self.bpm)
        track.append(tempo)
        
        rest = 1
        for i in range(len(self.noteName)):
            
            if self.noteName[i] == None:
                self.rest += 1
            else:
                self.rest = 1

            for j in range(len(self.noteName[i])):
                on = midi.NoteOnEvent(tick = 0, velocity = self.constVelocity, pitch = self.noteName[i][j] - 12)
                track.append(on)

            for k in range(len(self.noteName[i])):
                
                if k == 0:
                    off = midi.NoteOffEvent(tick = self.rest * self.resolution, pitch = self.noteName[i][k] - 12)
                else:
                    off = midi.NoteOffEvent(tick = 0, pitch = self.noteName[i][k] - 12)

                track.append(off)

        # create eot
        print("creating eot...")
        eot = midi.EndOfTrackEvent(tick = 1)
        track.append(eot)

        print ("This is the pattern")
        print (pattern)
        
        # save the pattern to ./output.mid
        print ("Saving ...")
        midi.write_midifile("output.mid", pattern)

        print ("Conversion finished")

'''
print ("running test")


notes = [[31, 57], [69], [48, 38]]

print(frequencyToNote([[440,220],[329.628,493.883]]))
'''
test = ConvertToMidi([[392.0],[440.0],[494.6666666],[522.6666666666666666666666], None, [440.0]], 90)
test.toMidi()

print("Test finished")
