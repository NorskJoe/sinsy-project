# 3 Processing MusicXML Files With Sinsy Website

There are two options for generating sound files with Sinsy.

One option is to download the source, compile, and run it on your machine
locally. The source is available at

[http://sinsy.sourceforge.net](http://sinsy.sourceforge.net)

Only the Japanese voice model is available for generating sound files
locally

The second option is to send the MusicXML file to the Sinsy website, and
to download the generated WAV file. More voice models are available, but
the Sinsy website is not always working. The Sinsy website is located at:

[http://sinsy.jp](http://sinsy.jp)

This can be done manually, or the ```upload.py``` script can be used to
automate this process.

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

