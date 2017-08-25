# 1 Splitting Multiple Parts Of MusicXML File

The scripts ```listPart.py``` and ```keepPart.py``` will allow you to
split a MusicXML file.

Generally you would run ```listPart.py``` to list all of the Part ID's
that are found in the MusicXML file.

Then you would use that Part ID with ```keepPart.py``` to process the
MusicXML file. It will output a new MusicXML file which only contains
the specified Part ID and filtering out the other parts. The old MusicXML
file is unaltered and remains intact.

The following explains how to use ```listPart.py``` and ```keepPart.py```

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

