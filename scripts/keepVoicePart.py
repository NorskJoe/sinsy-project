#!/usr/bin/python

import argparse
import xml.etree.ElementTree as ET

def keepVoicePart(root, voiceToKeep, partid):
    #
    # Remove unwanted tags:
    #
    # <part-list>
    #  <part-group/>    <-- these ones
    #  <score-part id="partid">    <-- these ones
    #  </score-part>    <-- this also
    # </part-list>
    #

    for a in root.findall('part-list'):
        for b in a.findall('score-part'):
            if b.attrib['id'] != partid:
                a.remove(b)
        for b in a.findall('part-group'):
            a.remove(b)

    #
    # Remove unwanted <part id="partid"> tags
    #
    # Also remove unwanted <note> tags associated with voice
    #

    for a in root.findall('part'):
#        print "part", a.attrib['id']
        if a.attrib['id'] != partid:
            # remove this <part> tag
#            print "removing", a.attrib['id']
            root.remove(a)
        else:
            # look for <note> tags in this part
            for b in a.findall('measure'):
                for c in b.findall('note'):
                    voice = None
                    for d in c.findall('voice'):
                        voice = d.text
                    if voice != voiceToKeep:
                        c.remove(d)

            



#
# Parse command line arguments
#

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("xmlfile", type=argparse.FileType('r'), help="name of the xml file or - for stdin")
    parser.add_argument("voice", help="voice to keep")
    parser.add_argument("partid", help="id of part to keep")
    args = parser.parse_args()

    #
    # Parse XML
    #

    root = ET.fromstring(args.xmlfile.read())

    keepVoicePart(root, args.voice, args.partid)

    #
    # Output modified XML
    #

#    print """<?xml version="1.0" encoding='UTF-8' standalone='no' ?>
#<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">"""
    print ET.tostring(root, encoding='UTF-8')

