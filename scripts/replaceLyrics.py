#!/usr/bin/python

import argparse
import xml.etree.ElementTree as ET

def replaceLyrics(root, replaceString):
    for a in root.findall('part'):
        for b in a.findall('measure'):
            for c in b.findall('note'):
                for d in c.findall('lyric'):
                    for e in d.findall('text'):
                        e.text = replaceString


#
# Parse command line arguments
#

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("xmlfile", type=argparse.FileType('r'), help="name of the xml file or - for stdin")
    parser.add_argument("replace", help="replace lyrics with this string")
    args = parser.parse_args()

    #
    # Parse XML
    #

    root = ET.fromstring(args.xmlfile.read())
    replaceLyrics(root, args.replace.decode('UTF-8'))

    #
    # Output modified XML
    #

#    print """<?xml version="1.0" encoding='UTF-8' standalone='no' ?>
#<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">"""
    print ET.tostring(root, encoding='UTF-8')

