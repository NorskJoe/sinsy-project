#!/usr/bin/python

import argparse
import xml.etree.ElementTree as ET

staccatoLookupTable = {
    'whole': 'half',
    'half': 'quarter',
    'quarter': 'eighth',
    'eighth': '16th',
    '16th': '32nd',
    '32nd': '64th',
    '64th': '128th',
    '128th': '256th',
    '256th': '512th',
    '512th': '1024th'
}

def shortenStaccatoNotes(root):
    for a in root.findall('part'):
        for b in a.findall('measure'):
            for c in b.findall('note'):
                staccato = False
                for d in c.findall('notations'):
                    for e in d.findall('articulations'):
                        for f in e.findall('staccato'):
                            staccato = True
                if not staccato:
                    continue
                type = None
                for d in c.findall('type'):
                    if staccatoLookupTable[d.text]:
                        type = staccatoLookupTable[d.text]
                        d.text = type
                duration = None
                for d in c.findall('duration'):
                    duration = str(int(d.text)/2)
                    d.text = duration
                instrument = None
                for d in c.findall('instrument'):
                    instrument = d.attrib['id']
                voice = None
                for d in c.findall('voice'):
                    voice = d.text
                staff = None
                for d in c.findall('staff'):
                    staff = d.text
                restNoteElt = ET.Element('note')
                ET.SubElement(restNoteElt, 'rest')
                if duration != None:
                    durationElt = ET.SubElement(restNoteElt, 'duration')
                    durationElt.text = duration
                if instrument != None:
                    instrumentElt = ET.SubElement(restNoteElt, 'instrument')
                    instrumentElt.attrib['id'] = instrument
                if voice != None:
                    voiceElt = ET.SubElement(restNoteElt, 'voice')
                    voiceElt.text = voice
                typeElt = ET.SubElement(restNoteElt, 'type')
                typeElt.text = type
                if staff != None:
                    staffElt = ET.SubElement(restNoteElt, 'staff')
                    staffElt.text = staff
                index = list(b).index(c)
                b.insert(index+1, restNoteElt)
                


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

    shortenStaccatoNotes(root)

    #
    # Output modified XML
    #

#    print """<?xml version="1.0" encoding='UTF-8' standalone='no' ?>
#<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">"""
    print ET.tostring(root, encoding='UTF-8')

