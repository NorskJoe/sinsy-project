# A Misc

These are miscellaneous scripts.

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
<!-- @Arthur - is there a limit to how many half steps we can alter? -->

Example usage:

This will shift it up 4 half steps.

> $ python replaceWithHarmony input.xml 4

This will shift it down 4 half steps.

> $ python replaceWithHarmony input.xml -4
