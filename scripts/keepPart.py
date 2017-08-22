#!/usr/bin/python

import sys
import argparse
import xml.etree.ElementTree as ET

def keepPart(root, partid):
    #
    # Remove unwanted tags:
    #
    # <part-list>
    #  <part-group/>    <-- these ones
    #  <score-part id="partid">    <-- these ones
    #  </score-part>    <-- this also
    # </part-list>
    #

#    print root.tag
    success = False
    for a in root.findall('part-list'):
#        print "a", a
        for b in a.findall('score-part'):
#            print "b", b
            if b.attrib['id'] != partid:
                a.remove(b)
            else:
                success = True
        for b in a.findall('part-group'):
            a.remove(b)

    #
    # Remove unwanted <part id="partid"> tags
    #

    for a in root.findall('part'):
#        print "part", a.attrib['id']
        if a.attrib['id'] != partid:
#            print "removing", a.attrib['id']
            root.remove(a)

    if not success:
        sys.exit("Part ID '" + partid + "' does not exist")

#
# Parse command line arguments
#

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("xmlfile", type=argparse.FileType('r'), help="name of the xml file or - for stdin")
    parser.add_argument("partid", help="id of part to keep")
    args = parser.parse_args()

    #
    # Parse XML
    #

    root = ET.fromstring(args.xmlfile.read())

    keepPart(root, args.partid)

    #
    # Output modified XML
    #

#    print """<?xml version="1.0" encoding='UTF-8' standalone='no' ?>
#<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">"""
    print ET.tostring(root, encoding='UTF-8')

