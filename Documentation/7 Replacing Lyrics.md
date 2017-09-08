# 7 Replacing Lyrics

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

## replaceLyrics.py

This will replace all the lyrics text with the specified string.

```
usage: replaceLyrics.py [-h] xmlfile lyrics

positional arguments:
  xmlfile     name of the xml file or - for stdin
  lyrics      replace lyrics with new lyrics, syllables separated by
              whitespace, in a single argument enclosed in quotes

optional arguments:
  -h, --help  show this help message and exit
```

Example usage:

> $ python replaceLyrics.py input.xml la

### Changing All The Lyrics

If you wanted to change all the lyrics in the text, first you could extract
the lyrics using ```printLyrics.py```:

```
python printLyrics.py Fragments.xml >lyrics.txt
```

The ```lyrics.txt``` file should look like this:

```
a a o o a a o o a a o o a a o o oh oh no no ah oh oh no oh oh oh oh oh oh oh oh or or or or all all or or or or oh, oh, oh, oh, e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e a, ow, a, ow, a, ow, a, ow, oh, oh, oh, oh, or or or or or or raw, a do, a do, a do, a do, or or or or or or, or or or, or or or, end, end, end, end, here, he, he, he, wall, wall, wall, wall, hell, hell, hell, hell, no, no, no, no, do no, do no, do no, do no, where, where, or or or, own n, war, wal low, oh, oh, hand le, hand le, head on, hand le, hand le, head on, dare he, dare he, won her, won her, done her, done her, hell done, hell done n raw howl, we warned, we'll drone n n n we'll drone n n n we'll drone n n n we'll drone n n n we'll drone n n n we'll drone n n n o o a a o o o o a a o o oh oh no no ah oh oh no no no no no no no no no no no no no or or or or or or or all or all or or or or oh oh, oh, oh, e e e e e e e e e e e e e e e e e e e e e e e e e e e e a, ow, a, ow, a, ow, a, ow, o o, o o, o o, o o, or, or, or or, or, or or, or, or or, or, or oo, oo, oo, oo, oo, oo, oo, oo, oo, oo, oo, oo, or or or or or or, or or or, or or or, e e e e he, here, he, here, or all, or all, or all, or all, e ell, e ell, e ell, e ell, no, no, no, no, no, no, no, no, air, air, air, air, or, a lone n, or, d low, oh, oh, and, and, don, and, and, don, e air, ee ee, e air, ee ee, were no, were no, no where, no where, now here, now here, we ee ee war or or we ee ee war or or or we warned, we warned, we warned, we'll drone n wan der hole, no where lad, no where lad, no where lad, we'll drone n n n we'll drone n n n d d d d d d d d he he he he he he he he or or or or war, war, war, war, woe, woe, woe, woe, e e e e e e e e end, end, end, end, a, ow a, ow a, ow a, ow low, low, low, low, raw, raw, raw, raw, do, do, do, do, law, law, law, law, rend, rend, rend, rend, he, he, here, here, or, all, or, all, or, all, or, all, e ell, e ell, e ell, e ell, oh oh oh oh do, do, do, do, air, air, air, air, or, own n, or oh, oh, oh, oh, oh, oh, and, and, o, o, o, o, o, on, and, and, o, o, o, o, o, on, air, ee, air, ee, er, er, er, oh, oh, oh, er, er, er, oh, oh, oh, no, e air, no, e air, ow, ere, ow, ere, we'll warn, we'll warn, or d we warned, we warned, we'll drone n n n we'll drone n n n we'll drone n n n we'll drone n n n we'll drone n n n we'll drone n n n n n n how, how, how, how, n, n, do, law, n, n, wall, wall, wall, wall, hell, oh oh oh oh nn, where, where, whore, lone n, warn d, n, n, n, dare he, dare he, her, her, er, er, her, her, er, er, e e ell, u u un, e e ell, u u un n or or or or or or a a a a a owl, we warned, we'll drone n n n we'll drone n n n we'll drone n n n we'll drone n n n we'll drone n n n we'll drone n n n
```

If you wanted to change all of the **a**'s to **uh**'s, then you could use
this command:

```
cat lyrics.txt | sed 's/a/uh/g' >newLyrics.txt
```

Finally, these new lyrics can be fed back into the XML file:

```
python replaceLyrics.py Fragments.xml "`cat newLyrics.txt`" >FragmentsWithNewLyrics.xml
```



