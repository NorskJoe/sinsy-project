#!/usr/bin/python

import argparse
import xml.etree.ElementTree as ET

def listParts(tree):
    root = tree.getroot()

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
            print partid, partname

#
# Parse command line arguments
#

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("xmlfile", help="name of the xml file")
    args = parser.parse_args()
    tree = ET.parse(args.xmlfile)
    listParts(tree)

