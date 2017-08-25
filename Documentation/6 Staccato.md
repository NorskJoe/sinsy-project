# 6 Staccato

For staccato notes, the ```shortenStaccatoNotes.py``` will halve the length
of notes labelled as staccato.

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

