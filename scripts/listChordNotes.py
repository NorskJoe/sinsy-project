#!/usr/bin/python

import argparse
import xml.etree.ElementTree as ET

def printNotes(root):
    for a in root.findall('part'):
        for b in a.findall('measure'):
            numberOfChordNotes = 0
            maxChordNotes = 0
            for c in b.findall('note'):
                isChord = False
                isRest = False
                for d in c.findall('rest'):
                    isRest = True
                for d in c.findall('chord'):
                    isChord = True
                if isRest:
                    numberOfChordNotes = 0
                    continue
                if isChord:
                    numberOfChordNotes += 1
                    if numberOfChordNotes > maxChordNotes:
                        maxChordNotes = numberOfChordNotes
                    continue
                numberOfChordNotes = 0
            if maxChordNotes > 0:
                print 'id', a.attrib['id'], 'measure', b.attrib['number'], maxChordNotes


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

