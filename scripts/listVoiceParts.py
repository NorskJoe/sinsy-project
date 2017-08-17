#!/usr/bin/python

import argparse
import xml.etree.ElementTree as ET

def listVoiceParts(root):
    results = {}
    for a in root.findall('part'):
        for b in a.findall('measure'):
            for c in b.findall('note'):
                for d in c.findall('voice'):
                    key = d.text + ' ' + a.attrib['id']
                    results[key] = 1
    print "Each voice is associated with a part"
    print "Example: '1 P1' means voice '1' part 'P1'"
    print

    allKeys = sorted(results.keys())
    print "\n".join(allKeys)

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

    listVoiceParts(root)

