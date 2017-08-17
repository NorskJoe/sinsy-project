#!/usr/bin/python

import argparse
import xml.etree.ElementTree as ET

def printLyrics(root):
    results = []
    for a in root.findall('part'):
        for b in a.findall('measure'):
            for c in b.findall('note'):
                for d in c.findall('lyric'):
                    for e in d.findall('text'):
                        results.append(e.text.encode('UTF-8'))

    print " ".join(results)

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

    printLyrics(root)

