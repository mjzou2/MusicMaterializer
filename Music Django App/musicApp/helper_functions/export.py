# import music21
# from music21 import *
# music21.environment.set('autoDownload', 'allow')
# music21.environment.set('lilypondFormat', 'pdf')
# music21.environment.UserSettings().['lilypondPath'] =
# '/usr/local/lib/python3.6/dist-packages/music21/lily/'

# Parses the MIDI file. Param should be a file path or URL.

# Right now the link leads to the Super Mario theme, but we can eventually replace it with our
# desired MIDI file. Seems to work as intended.
# stream1 = music21.converter.parse('https://bitmidi.com/uploads/37900.mid',format='MIDI')

# Takes the MIDI file that we entered and displays text showing the notes in order.
# Warning: output is very long.
# stream1.show('text')
# Takes the parsed MIDI file and converts it to a pdf thru lilypond. Doesn't quite work yet.
# Need to read up more on LilyPond integration before this will work, I think.
# lilyFile = stream1.write('lily')
import subprocess
import sys
from pprint import pprint
import os
import base64
import flat_api
from flat_api.rest import ApiException


configuration = flat_api.Configuration()
configuration.access_token = 'd2cca9a3f1c34d470530e4c38068ef56ddd0a25c2bd3838af7592192f8db08f18d084ac8961849b3b14842d4aaebd9e33bccabd83d6d57843f3ecc319e656627'
flat_api_client = flat_api.ApiClient(configuration)
api_instance = flat_api.AccountApi(flat_api_client)


def export_to_flat(name, file, apikey):
    try:
        # Get current user profile
        # api_response = api_instance.get_authenticated_user()
        # pprint(api_response)

        configuration.access_token = apikey

        f = open(file, 'rb')
        contents = base64.b64encode(f.read()).decode('ascii')
        # The new score meta, including the MusicXML file as `data`
        new_score = flat_api.ScoreCreation(
            title=name,
            privacy='public',
            data_encoding='base64',
            data=contents
        )

        # Create the document and print the meta returned by the API
        pprint(flat_api.ScoreApi(flat_api_client).create_score(new_score))
    except (ApiException) as e:
        print(e)
    except Exception as e:
        print(e)

def export_to_pdf(output_file):
    subprocess.run(["bash", "midi-to-pdf.sh", output_file])

