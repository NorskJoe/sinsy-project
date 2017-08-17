#!/usr/bin/python

import argparse
import xml.etree.ElementTree as ET

def printNotes(root):
    for a in root.findall('part'):
        for b in a.findall('measure'):
            for c in b.findall('note'):
                type = None
                for d in c.findall('type'):
                    type = d.text
                duration = None
                for d in c.findall('duration'):
                    duration = d.text
                for d in c.findall('notations'):
                    for e in d.findall('articulations'):
                        for f in e.findall('staccato'):
                            print "part", a.attrib['id'], "measure", b.attrib['number'], "type", type, "duration", duration, "staccato", "index", b.getchildren().index(c)


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

