# accepts a MIDI file and outputs a pdf using lilypond
midi2ly $1 --output=music.ly
lilypond music.ly
rm music.ly
rm music.midi
