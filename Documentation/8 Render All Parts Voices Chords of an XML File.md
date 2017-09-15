# 8 Render All Parts Voices Chords of an XML File

## renderAllPartsVoicesChords.py

This will generate a shell script to render all parts, voices, and chords
in an XML file.

```
usage: renderAllPartsVoicesChords.py [-h] xmlfile outputdir

positional arguments:
  xmlfile     name of the xml file
  outputdir   name of the directory to use for the temporary files and final
              WAV file

optional arguments:
  -h, --help  show this help message and exit
```

Example usage:

> $ python renderAllPartsVoicesChords.py Fragments.xml tempdir >fragments.sh

The output ```fragments.sh``` will be a shell script:

```
# Output directory: tempdir
mkdir "tempdir"
#
# Rendering for the following parts:
#    {'chord': False, 'voice': '1', 'part': 'P1'}
python keepPart.py "Fragments.xml" P1 >"tempdir/P1-1.xml"
python upload.py "tempdir/P1-1.xml" "tempdir/P1-1.wav"
#    {'chord': True, 'voice': '1', 'part': 'P1'}
python keepPart.py "Fragments.xml" P1 | python useChordNotes.py >"tempdir/P1-1-chord.xml"
python upload.py "tempdir/P1-1-chord.xml" "tempdir/P1-1-chord.wav"
#    {'chord': False, 'voice': '1', 'part': 'P2'}
python keepPart.py "Fragments.xml" P2 >"tempdir/P2-1.xml"
python upload.py "tempdir/P2-1.xml" "tempdir/P2-1.wav"
#    {'chord': True, 'voice': '1', 'part': 'P2'}
python keepPart.py "Fragments.xml" P2 | python useChordNotes.py >"tempdir/P2-1-chord.xml"
python upload.py "tempdir/P2-1-chord.xml" "tempdir/P2-1-chord.wav"
#    {'chord': False, 'voice': '1', 'part': 'P3'}
python keepPart.py "Fragments.xml" P3 >"tempdir/P3-1.xml"
python upload.py "tempdir/P3-1.xml" "tempdir/P3-1.wav"
#    {'chord': True, 'voice': '1', 'part': 'P3'}
python keepPart.py "Fragments.xml" P3 | python useChordNotes.py >"tempdir/P3-1-chord.xml"
python upload.py "tempdir/P3-1-chord.xml" "tempdir/P3-1-chord.wav"
#    {'chord': False, 'voice': '1', 'part': 'P4'}
python keepPart.py "Fragments.xml" P4 >"tempdir/P4-1.xml"
python upload.py "tempdir/P4-1.xml" "tempdir/P4-1.wav"
#    {'chord': True, 'voice': '1', 'part': 'P4'}
python keepPart.py "Fragments.xml" P4 | python useChordNotes.py >"tempdir/P4-1-chord.xml"
python upload.py "tempdir/P4-1-chord.xml" "tempdir/P4-1-chord.wav"
# Mix
sox -m "tempdir/P1-1.wav" "tempdir/P1-1-chord.wav" "tempdir/P2-1.wav" "tempdir/P2-1-chord.wav" "tempdir/P3-1.wav" "tempdir/P3-1-chord.wav" "tempdir/P4-1.wav" "tempdir/P4-1-chord.wav" "tempdir/mix.wav"
sox "tempdir/mix.wav" "tempdir/norm.wav" gain -n
sox "tempdir/norm.wav" "tempdir/reverb.wav" reverb
python soxCompand.py "tempdir/reverb.wav" "tempdir/output.wav"
```

You can tweak this script to your liking. 
The final output will be ```tempdir/output.wav```.

