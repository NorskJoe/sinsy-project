#!/usr/bin/python

import argparse
import xml.etree.ElementTree as ET

def printNotes(root):
    for a in root.findall('part'):
        for b in a.findall('measure'):
            for c in b.findall('note'):
                for d in c.findall('pitch'):
                    step = ''
                    octave = 0
                    alter = 0
                    for e in d.findall('step'):
                        step = e.text
                    for e in d.findall('alter'):
                        alter = int(e.text)
                    for e in d.findall('octave'):
                        octave = int(e.text)
                    print "step", step, "alter", alter, "octave", octave


#
# Parse command line arguments
#

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("xmlfile", nargs='?', type=argparse.FileType('r'), default='-', help="name of the xml file or - for stdin")
    args = parser.parse_args()

    #
    # Parse XML
    #

    root = ET.fromstring(args.xmlfile.read())

    printNotes(root)

