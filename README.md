# sinsy-project

Programming Project 1

Sinsy is a HMM-based Singing Voice Synthesis System that uses MusicXML files
as input. Herein lies some Python scripts for dealing with said files.

The following is a list of the scripts and their function.

## keepPart.py

Each XML file has one or more parts. Sinsy will only render only one part
at a time, so if an XML file has more than one part, it is necessary to
split it up so that all the parts get rendered separately. Conveniently,
this script will help accomplish that task.

```
usage: keepPart.py [-h] xmlfile partid

positional arguments:
  xmlfile     name of the xml file or - for stdin
  partid      id of part to keep

optional arguments:
  -h, --help  show this help message and exit
```

Example usage:

> $ python keepPart.py input.xml P1

This will read the `input.xml` file and extract the part `P1`.

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

## listPart.py

This will list all the parts in an XML file.

```
usage: listParts.py [-h] [xmlfile]

positional arguments:
  xmlfile     name of the xml file or - for stdin

optional arguments:
  -h, --help  show this help message and exit
```

Example usage:

> $ python listParts.py input.xml

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


## printDynamics.py

This will extract and print the dynamics tags (like p, mp, f) in an XML file.

```
usage: printDynamics.py [-h] [xmlfile]

positional arguments:
  xmlfile     name of the xml file or - for stdin

optional arguments:
  -h, --help  show this help message and exit
```

Example usage:

> $ python printDynamics.py input.xml

## printLyrics.py

This will extract and print the lyric tags in an XML file.

```
usage: printLyrics.py [-h] [xmlfile]

positional arguments:
  xmlfile     name of the xml file or - for stdin

optional arguments:
  -h, --help  show this help message and exit
```

Example usage:

> $ python printLyrics.py input.xml

## printNotes.py

This will extract and print the note/pitch tags in an XML file.

```
usage: printNotes.py [-h] [xmlfile]

positional arguments:
  xmlfile     name of the xml file or - for stdin

optional arguments:
  -h, --help  show this help message and exit
```

Example usage:

> $ python printNotes.py input.xml

## printStaccatoNotes.py

This will extract and print the stacatto note tags in an XML file.

```
usage: printStaccatoNotes.py [-h] [xmlfile]

positional arguments:
  xmlfile     name of the xml file or - for stdin

optional arguments:
  -h, --help  show this help message and exit
```

Example usage:

> $ python printStaccatoNotes.py input.xml

## replaceLyrics.py

This will replace all the lyrics text with the specified string.

```
usage: replaceLyrics.py [-h] xmlfile replace

positional arguments:
  xmlfile     name of the xml file or - for stdin
  replace     replace lyrics with this string

optional arguments:
  -h, --help  show this help message and exit
```

Example usage:

> $ python replaceLyrics.py input.xml la

## replaceWithHarmony.py

This will shift the pitch of all the notes up or down N semitones or half
steps (which ever you want to call it). There are 12 semitones in an octave.

```
usage: replaceWithHarmony.py [-h] xmlfile halfsteps

positional arguments:
  xmlfile     name of the xml file or - for stdin
  halfsteps   number of half steps +/-

optional arguments:
  -h, --help  show this help message and exit
```

Example usage:

This will shift it up 4 half steps.

> $ python replaceWithHarmony input.xml 4

This will shift it down 4 half steps.

> $ python replaceWithHarmony input.xml -4

## shortenStaccatoNotes.py

This will take all notes that are labelled as staccato, make it so that
their length is halved, and followed by a rest of the same length.

```
usage: shortenStaccatoNotes.py [-h] [xmlfile]

positional arguments:
  xmlfile     name of the xml file or - for stdin

optional arguments:
  -h, --help  show this help message and exit
```

Example usage:

> $ python shortenStaccatoNotes.py input.xml

## soxCompand.py

This will run the `compand (dynamic compression)` effect using `sox` with the
default parameters, on the specified .WAV file.

```
usage: soxCompand.py [-h] infile outfile

positional arguments:
  infile      name of input file
  outfile     name of output file

optional arguments:
  -h, --help  show this help message and exit
```

Example usage:

> $ python soxCompand.py input.wav output.wav

## upload.py

This will send an XML file for processing to the Sinsy website, and download
the resulting generated .WAV file.

```
usage: upload.py [-h] [--spkrlang SPKRLANG] [--spkr SPKR]
                 [--synalpha SYNALPHA] [--vibpower VIBPOWER]
                 [--f0shift F0SHIFT]
                 infile outfile

positional arguments:
  infile               name of the input xml file
  outfile              name of the output wave file

optional arguments:
  -h, --help           show this help message and exit
  --spkrlang SPKRLANG  speaker language, 'english', 'japanese', or 'mandarin'
  --spkr SPKR          speaker, default is 4, Japanese voices: 0=Yoko 1=Xiang-
                       Ling 2=Namine Ritsu S 3=undefined 7=Yoko DNN, English
                       voices: 4=Xiang-Ling 5=Matsuo-P, Mandarin voices: 6
                       =Xiang-Ling
  --synalpha SYNALPHA  synalpha, default is 0.55
  --vibpower VIBPOWER  vibpower, default is 1
  --f0shift F0SHIFT    f0shift, default is 0
```

Example usage:

> $ python upload.py --spkrlang english --spkr 4 --synalpha 0.55 --vibpower 1 --f0shift 0 input.xml output.wav

