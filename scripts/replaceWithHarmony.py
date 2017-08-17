#!/usr/bin/python

import argparse
import xml.etree.ElementTree as ET

def parseNote(note, alter, octave, delta):
    notes = [ 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B' ]
    numberOfNotes = len(notes)
    index = notes.index(note)
    index += alter
    index += delta
    while index < 0:
        index += numberOfNotes
        octave -= 1
    while index >= numberOfNotes:
        index -= numberOfNotes
        octave += 1
    newNote = notes[index][0]
    newAlter = 0
    if len(notes[index]) > 1:
        newAlter = 1
    return newNote, newAlter, octave
    
def testParseNote():
    for note in "ABCDEFG":
        for alter in [ -1, 0, 1 ]:
            newNote, newAlter, newOctave = parseNote(note, alter, 4, 4)
            print "note", note, "alter", alter, "octave 4", "->", "newNote", newNote, "newAlter", newAlter, "newOctave", newOctave

def replaceWithHarmony(root, delta):
    for a in root.findall('part'):
        for b in a.findall('measure'):
            for c in b.findall('note'):
                for d in c.findall('pitch'):
                    step = ''
                    octave = 0
                    alter = 0
                    for e in d.findall('step'):
                        step = e.text
                    for e in d.findall('alter'):
                        alter = int(e.text)
                    for e in d.findall('octave'):
                        octave = int(e.text)
                    newNote, newAlter, newOctave = parseNote(step, alter, octave, delta)
                    for e in d.findall('step'):
                        e.text = newNote
                    for e in d.findall('alter'):
                        e.text = str(newAlter)
                    for e in d.findall('octave'):
                        e.text = str(newOctave)

                    alterTag = d.find('alter')
                    if alterTag == None:
                        e = d.makeelement('alter', {})
                        d.append(e)
                        e.text = str(newAlter)


#
# Parse command line arguments
#

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("xmlfile", type=argparse.FileType('r'), help="name of the xml file or - for stdin")
    parser.add_argument("halfsteps", help="number of half steps +/-")
    args = parser.parse_args()

    #
    # Parse XML
    #

    root = ET.fromstring(args.xmlfile.read())
    replaceWithHarmony(root, int(args.halfsteps))

    #
    # Output modified XML
    #

#    print """<?xml version="1.0" encoding='UTF-8' standalone='no' ?>
#<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">"""
    print ET.tostring(root, encoding='UTF-8')
