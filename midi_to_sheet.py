import music21
from music21 import *
music21.environment.set('autoDownload', 'allow')
music21.environment.set('lilypondFormat', 'pdf')

# Parses the MIDI file. Param should be a file path or URL.

# Right now the link leads to the Super Mario theme, but we can eventually replace it with our
# desired MIDI file. Seems to work as intended.
stream1 = music21.converter.parse('https://bitmidi.com/uploads/98137.mid',format='MIDI')

# Takes the MIDI file that we entered and displays text showing the notes in order.
# Warning: output is very long.
stream1.show('text')

# Takes the parsed MIDI file and converts it to a pdf thru lilypond. Doesn't quite work yet.
# Need to read up more on LilyPond integration before this will work, I think.
stream1.write('lily.pdf')
