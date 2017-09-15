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

## generateStochasticSong.py

This will generate an stochastic song based on the name and lyrics given in
the arguments. Make sure you have enough lyrics for a song (about 60
syllables should be enough). If there are unrecognized words you will have
to add them to the syllable dictionary in the script.

```
usage: generateStochasticSong.py [-h] songname lyricsfile [scale]

positional arguments:
  songname    name of the song
  lyricsfile  name of the lyrics file
  scale       'major', 'minor', or 'blues', default is 'major'

optional arguments:
  -h, --help  show this help message and exit
```

Example usage:

First generate some lyrics using the weather script:

> $ python retrieveWeatherData.py London >lyrics.txt

Then use those lyrics to generate the song:

> $ python generateStochasticSong.py London lyrics.txt major >london.xml

It sounds better if you turn the volume all the way down to -11.

