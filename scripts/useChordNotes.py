#!/usr/bin/python

import argparse
import xml.etree.ElementTree as ET

def useChordNotes(root):
    for a in root.findall('part'):
        for b in a.findall('measure'):
            for c in b.findall('note'):
                isChord = False
                for d in c.findall('chord'):
                    isChord = True
                if isChord:
                    continue
                for d in c.findall('pitch'):
                    c.remove(d)
                ET.SubElement(c, 'restyyy')
    for a in root.findall('part'):
        for b in a.findall('measure'):
            originalNoteElement = None
            for c in b.findall('note'):
                isChord = False
                for d in c.findall('chord'):
                    isChord = True
                if not isChord:
                    originalNoteElement = c
                    continue
                if originalNoteElement != None:
                    for d in originalNoteElement.findall('pitch'):
                        originalNoteElement.remove(d)
                    for d in c.findall('pitch'):
                        originalNoteElement.insert(0, d)
                    b.remove(c)
#                print 'id', a.attrib['id'], 'measure', b.attrib['number'], numberOfChordNotes, "voice", voice, "lyric", lyric
                


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
    useChordNotes(root)

    #
    # Output modified XML
    #

#    print """<?xml version="1.0" encoding='UTF-8' standalone='no' ?>
#<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">"""
    print ET.tostring(root, encoding='UTF-8')

