# 2 Audio Mixing With SoX

From the SoX home page:

> SoX is a cross-platform (Windows, Linux, MacOS X, etc.) command line utility that can convert various formats of computer audio files in to other formats. It can also apply various effects to these sound files, and, as an added bonus, SoX can play and record audio files on most platforms. 

[http://sox.sourceforge.net](http://sox.sourceforge.net)

## Mixing Multiple WAV Files

Let's say you have three WAV files:

- vocals.wav
- piano.wav
- drums.wav

The simplest way to mix them is with this command:

```
sox -m vocals.wav piano.wav drums.wav output.wav
```

This will use those files as input and the result will be ```output.wav```.
Generally these files will be mono. If you want to mix stereo, you'll
have to specify if you want to pan left or right.

## Adding reverb

The simplest way to add reverb is with this command:

```
sox vocals.wav output.wav reverb
```

## Dynamic compression

### soxCompand.py

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

