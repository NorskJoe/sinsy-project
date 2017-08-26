#!/usr/bin/python

import re
import argparse
import xml.etree.ElementTree as ET

def replaceLyrics(root, lyrics):
    n = len(lyrics)
    i = 0
    for a in root.findall('part'):
        for b in a.findall('measure'):
            for c in b.findall('note'):
                hasRest = False
                for d in c.findall('rest'):
                    hasRest = True
                if hasRest:
                    continue
                hasLyric = False
                for d in c.findall('lyric'):
                    hasLyric = True
                if not hasLyric:
                    lyricElt = ET.SubElement(c, 'lyric')
                for d in c.findall('lyric'):
                    hasLyricText = False
                    for e in d.findall('text'):
                        hasLyricText = True
                    if not hasLyricText:
                        lyricTextElt = ET.SubElement(d, 'text')
                    for e in d.findall('text'):
                        e.text = lyrics[i%n]
                        i+=1


#
# Parse command line arguments
#

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("xmlfile", type=argparse.FileType('r'), help="name of the xml file or - for stdin")
    parser.add_argument("lyrics", help="replace lyrics with new lyrics, syllables separated by whitespace, in a single argument enclosed in quotes")
    args = parser.parse_args()

    lyrics = re.split(r'\s+', args.lyrics.decode('UTF-8'))

    #
    # Parse XML
    #

    root = ET.fromstring(args.xmlfile.read())
    replaceLyrics(root, lyrics)

    #
    # Output modified XML
    #

#    print """<?xml version="1.0" encoding='UTF-8' standalone='no' ?>
#<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">"""
    print ET.tostring(root, encoding='UTF-8')

