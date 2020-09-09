# Andrew Tian

# create ranges for frequencies to output a String result of the note
# for example: 120Hz-150Hz outputs G3
# use lazy_midi module that converts given frequencies to return MIDI pitch number

from audiolazy import freq2midi, freq2str, str2freq

"""
test = freq2midi(120)
print(test)

test2 = freq2str(120)
print(test2)

print(str2freq("F#2"))

print(freq2str(str2freq("F#2")))
"""

def frequencyToNote(frequencies):
	tempList = frequencies.copy()
	
	for i in range(len(frequencies)):
		tempList[i] = freq2str(frequencies[i])
	
	print(tempList)

def main():
	print("main run")

testList = [[120, 250, 40], [60, 100], [60, 230, 130]]
frequencyToNote(testList)

if __name__ == "__main__":
        main()
