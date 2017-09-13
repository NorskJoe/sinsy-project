#!/usr/bin/python

import random
import re
import argparse
import xml.etree.ElementTree as ET

def shiftNote(note, alter, octave, delta):
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
    
def generateXML(arr):
    score_partwise = ET.Element('score-partwise')
    part_list = ET.SubElement(score_partwise, 'part-list')
    score_part = ET.SubElement(part_list, 'score-part')
    score_part.attrib['id'] = 'P1'
    part = ET.SubElement(score_partwise, 'part')
    part.attrib['id'] = 'P1'
    measureNumber = 1
    measure = None
    for i in range(0, len(arr)):
        measure = ET.SubElement(part, 'measure')
        measure.attrib['number'] = str(measureNumber)
        if measureNumber == 1:
            direction = ET.SubElement(measure, 'direction')
            sound = ET.SubElement(direction, 'sound')
            sound.attrib['tempo'] = '195'
        measureNumber += 1
        note = ET.SubElement(measure, 'note')
#        type = ET.SubElement(note, 'type')
#        type.text = 'quarter'
        duration = ET.SubElement(note, 'duration')
        duration.text = '12'
        voice = ET.SubElement(note, 'voice')
        voice.text = '1'
        pitch = ET.SubElement(note, 'pitch')
        step = ET.SubElement(pitch, 'step')
        alter = ET.SubElement(pitch, 'alter')
        octave = ET.SubElement(pitch, 'octave')
        newNote, newAlter, newOctave = shiftNote('C', 0, 4, arr[i])
        step.text = newNote
        alter.text = str(newAlter)
        octave.text = str(newOctave)

    return score_partwise

def generateStochasticMelody():
    scale = [-10, -8, -7, -5, -3, -1, 0, 2, 4, 5, 7, 9, 11]
    results = []
    current = 6
    for i in range(0, 31):
        results.append(scale[current])
        num = random.random()
        if num < 0.5:
            current -= 1
        else:
            current += 1
        if current < 0:
            current = 0;
        if current >= len(scale):
            current = len(scale)-1
    results.append(scale[6])
    return results

#
# Parse command line arguments
#

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    #
    # Parse XML
    #

    melody = generateStochasticMelody()
    root = generateXML(melody)

    #
    # Output modified XML
    #

#    print """<?xml version="1.0" encoding='UTF-8' standalone='no' ?>
#<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">"""
    print ET.tostring(root, encoding='UTF-8')

