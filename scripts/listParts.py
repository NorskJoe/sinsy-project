#!/usr/bin/python

import argparse
import xml.etree.ElementTree as ET

def listParts(root):
    #
    # The tags we are interested in:
    #
    # <part-list>
    #  <score-part id="Part ID">>
    #   <part-name>Part Name</part-name>
    #  </score-part>
    # </part-list>
    #

    print "List of Part ID's:"
#    print root.tag
    for a in root.findall('part-list'):
#        print "a ", a
        for b in a.findall('score-part'):
#            print "b ", b
            partid = b.attrib['id']
            partname = ''
            for c in b.findall('part-name'):
                partname = c.text
            print "Part ID:", partid, "  Part Name:", partname

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

    listParts(root)

