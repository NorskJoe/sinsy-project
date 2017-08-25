# 7 Misc

These are miscellaneous scripts.

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

