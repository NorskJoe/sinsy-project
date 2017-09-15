# 4 Multiple Simultaneous Notes In A Vocal Part

If there are multiple simultaneous notes in a vocal part, these are
represented in a MusicXML as separate <voice>'s and each voice is associated
with a part.

To split these out, run ```listVoiceParts.py``` to list all of the voices
and parts found in the MusicXML file. Then run ```keepVoicePart.py```
which will output a new MusicXML file with only the desired voice/part.

## listVoiceParts.py

This will list all the voices and their respective parts in an XML file.

```
usage: listVoiceParts.py [-h] [xmlfile]

positional arguments:
  xmlfile     name of the xml file or - for stdin

optional arguments:
  -h, --help  show this help message and exit
```

Example usage:

> $ python listVoiceParts.py input.xml


## keepVoicePart.py

Each part may have more than one voice. Generally, if there are multiple
simultaneous notes (i.e. a chord), each note will be represented by a
separate voice, so that each voice only contains a single note.

```
usage: keepVoicePart.py [-h] xmlfile voice partid

positional arguments:
  xmlfile     name of the xml file or - for stdin
  voice       voice to keep
  partid      id of part to keep

optional arguments:
  -h, --help  show this help message and exit
```

Example usage:

> $ python keepVoicePart.py input.xml 1 P1

This will read the `input.xml` file and extract voice `1` from part `P1`.

## useChordNotes.py

This script will replace the first note of the chord with the second note
of the chord, which may be better for rendering with Sinsy.

```
usage: useChordNotes.py [-h] [xmlfile]

positional arguments:
  xmlfile     name of the xml file or - for stdin

optional arguments:
  -h, --help  show this help message and exit
```

Example usage:

> $ python useChordNotes.py Fragments.xml

## useVoice.py

This script will replace the note for the first voice with the note for 
the specified voice, which may be better for rendering with Sinsy.

```
usage: useVoice.py [-h] xmlfile voice

positional arguments:
  xmlfile     name of the xml file or - for stdin
  voice       voice to use

optional arguments:
  -h, --help  show this help message and exit
```

Example usage:

> $ python useVoice.py moments.xml 2

