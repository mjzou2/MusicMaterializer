# accepts a MIDI file and outputs a pdf using lilypond
echo "converting midi to music.ly..."
midi2ly $1 --output=music.ly
echo "converting music.ly to pdf..."
lilypond music.ly
echo "Done."
rm music.ly
