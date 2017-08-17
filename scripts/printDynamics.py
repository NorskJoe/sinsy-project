#!/usr/bin/python

import argparse
import xml.etree.ElementTree as ET

def printDynamics(root):
    for a in root.findall('part'):
        for b in a.findall('measure'):
            for c in b.findall('direction'):
                for d in c.findall('direction-type'):
                    for e in d.findall('dynamics'):
                        for f in list(e):
                            print "part", a.attrib['id'], "measure", b.attrib['number'], "dynamics", f.tag
                    for e in d.findall('wedge'):
                        print "part", a.attrib['id'], "measure", b.attrib['number'], "wedge", e.attrib['type']


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

    printDynamics(root)

