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
            j = 0
            k = 0
            while j < len(frequencies[i]) - k:
                if tempList[i][j] < 0 or tempList[i][j] >= 256:
                    tempList[i].remove(tempList[i][j])
                    j = 0
                    k += 1
                j += 1
    print(tempList)
    return tempList


# convert the list of Midi numbers into a functional midi file
class ConvertToMidi:
    noteName = []
    bpm = 120
    constVelocity = 30
    resolution = 220
    export = ''
    onsets = []

    # constructor
    def __init__(self, notes, tempo, exports, onsets):
        print("constructing...")
        print(notes)
        print(onsets)

        self.noteName = frequencyToNote(notes)
        self.export = exports

        self.onsets = [ele * self.resolution * tempo / 60 for ele in onsets]
        self.onsets = [self.onsets[i] - self.onsets[i - 1] for i in range(1, len(onsets))]
        for i in range(len(self.noteName)):
            for j in range(len(self.noteName[i])):
                self.noteName[i][j] = round(self.noteName[i][j])

        self.bpm = tempo

    # convert notes and output the midi file
    def toMidi(self):
        print("called toMidi")
        print(self.onsets)
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

        rest = 0
        cont = 1
        onset_index = 0
        for i in range(len(self.noteName)):
            if self.noteName[i] == []:
                rest += 1
            else:
                progression = 0 + (rest * 55)
                on = midi.NoteOnEvent(tick=progression, velocity=self.constVelocity,
                                      pitch=self.noteName[i][0])
                track.append(on)
                rest = 0

                try:
                    if i < len(self.noteName) and not self.noteName[i + 1] == []\
                            and self.noteName[i][0] == self.noteName[i + 1][0]\
                            and not self.onsets[onset_index] - 25 <= cont * 55 <=\
                            self.onsets[onset_index] + 25:
                        cont += 1
                        continue
                except IndexError:
                    if not self.noteName[i + 1]:
                        break

                off = midi.NoteOffEvent(tick=cont * 55, pitch=self.noteName[i][0])
                track.append(off)
                cont = 1
                onset_index += 1

        # create eot
        print("creating eot...")
        eot = midi.EndOfTrackEvent(tick=1)
        track.append(eot)

        print("This is the pattern")
        print(pattern)

        # save the pattern to ./output.mid
        print("Saving ...")
        midi.write_midifile(self.export + '.mid', pattern)

        print("Conversion finished")


'''
print ("running test")


#notes = [[31, 57], [69], [48, 38]]

#print(frequencyToNote([[440,220],[329.628,493.883]]))

test = ConvertToMidi([[392.0,1.3333333333333,440],[440.0,1.333333333,16.35],[494.6666666,1.3333333333333],[522.6666666666666666666666,1.333333333], None, None, [440.0], None, None], 90)
test.toMidi()

print("Test finished")

print(frequencyToNote([[1.4444],[440],[494.66666],[522.6666666666, 1.33333333]]))
'''
