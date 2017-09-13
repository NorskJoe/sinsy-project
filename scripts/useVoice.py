#!/usr/bin/python

import argparse
import xml.etree.ElementTree as ET

def useVoice(root, voiceToKeep):
    if voiceToKeep == '1':
        return
    for a in root.findall('part'):
        for b in a.findall('measure'):
            pitches = {}
            duration = 0
            for c in b.findall('note'):
                voice = None
                for d in c.findall('voice'):
                    voice = d.text
                if voice == voiceToKeep:
                    for d in c.findall('pitch'):
                        pitches[str(duration)] = d
                    for d in c.findall('duration'):
                        duration += int(d.text)
            duration = 0
            for c in b.findall('note'):
                voice = None
                for d in c.findall('voice'):
                    voice = d.text
                if voice == '1':
                    for d in c.findall('pitch'):
                        if str(duration) in pitches:
                            c.remove(d)
                            c.append(pitches[str(duration)])
                    for d in c.findall('duration'):
                        duration += int(d.text)

#                print 'id', a.attrib['id'], 'measure', b.attrib['number'], numberOfChordNotes, "voice", voice, "lyric", lyric
                


#
# Parse command line arguments
#

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("xmlfile", type=argparse.FileType('r'), help="name of the xml file or - for stdin")
    parser.add_argument("voice", help="voice to use")
    args = parser.parse_args()

    #
    # Parse XML
    #

    root = ET.fromstring(args.xmlfile.read())
    useVoice(root, args.voice)

    #
    # Output modified XML
    #

#    print """<?xml version="1.0" encoding='UTF-8' standalone='no' ?>
#<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">"""
    print ET.tostring(root, encoding='UTF-8')

