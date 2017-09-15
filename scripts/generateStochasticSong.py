#!/usr/bin/python

import sys
import random
import re
import argparse
import xml.etree.ElementTree as ET
from addLyrics import addLyrics

syllableDictionary = {
'melbourne' : 'mell born',
'london' : 'lon don',
'the' : 'the',
'weather' : 'weh ther',
'is' : 'is',
'forecasted' : 'fore cas ted',
'to' : 'to',
'be' : 'be',
'partly' : 'part lee',
'cloudy' : 'clow dee',
'with' : 'with',
'daytime' : 'day time',
'temperature' : 'tem per a ture',
'reaching' : 'rea ching',
'c' : 'sell see us',
'night' : 'night',
'time' : 'time',
'are' : 'are',
'expected' : 'ex pec ted',
'cit' : 'cit',
'will' : 'will',
'stay' : 'stay',
'dry' : 'dry',
'no' : 'no',
'precipitation' : 'prih sih pih tay shun',
'visibility' : 'vih sih bil ih tee',
'going' : 'go ing',
'around' : 'uh round',
'km' : 'kee low mee ters',
'ie' : 'eye ee',
'miles' : 'my ules',
'and' : 'and',
'an' : 'an',
'atmospheric' : 'at moe sphere ick',
'pressure' : 'presh shure',
'of' : 'of',
'mb' : 'em bee',
'it' : 'it',
'cloud' : 'cloud',
'covering' : 'kah ver ring',
'sky' : 'sky',
'humidity' : 'hue mih dih tee',
'we' : 'we',
'expect' : 'ex pect',
'mm' : 'mill ih mee ters',
'fall' : 'fall',
'i' : 'eye',
'e' : 'ee',
}

def breakIntoSyllables(text):
    text = text.decode('UTF-8').lower()
    text = re.sub('[^a-zA-Z \n]', ' ', text)
    text = re.split(r'\s+', text)
    results = []
    for word in text:
        if not len(word):
            continue
        if word in syllableDictionary:
            results.extend(re.split(r'\s+', syllableDictionary[word]))
        else:
            print "The word '" + word + "' is not in the syllableDictionary."
            print "Add it by editing this script and then run it again."
            sys.exit(1)
    return results


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
            sound.attrib['tempo'] = '300'
        measureNumber += 1
        note = ET.SubElement(measure, 'note')
#        type = ET.SubElement(note, 'type')
#        type.text = 'quarter'
        duration = ET.SubElement(note, 'duration')
        duration.text = '12'
        voice = ET.SubElement(note, 'voice')
        voice.text = '1'
        if arr[i] == 99:
            rest = ET.SubElement(note, 'rest')
        else:
            pitch = ET.SubElement(note, 'pitch')
            step = ET.SubElement(pitch, 'step')
            alter = ET.SubElement(pitch, 'alter')
            octave = ET.SubElement(pitch, 'octave')
            newNote, newAlter, newOctave = shiftNote('C', 0, 4, arr[i])
            step.text = newNote
            alter.text = str(newAlter)
            octave.text = str(newOctave)

    return score_partwise

def generateStochasticMelody(scale, numberOfNotes):
    results = []
    for i in range(0, numberOfNotes):
        num = int(random.random() * len(scale))
        results.append(scale[num])
    return results

def generateStochasticSong(verseScale, chorusScale):
    riff = generateStochasticMelody(verseScale, 4)
    verse = []
    verse.extend(riff)
    verse.extend(riff)
    verse.extend(riff)
    verse.append(verseScale[0])
    verse.append(99)
    verse.append(99)
    verse.append(99)
    chorus = generateStochasticMelody(chorusScale, 7)
    chorus[0] = chorusScale[-1];
    chorus.append(99)
    song = []
    song.extend(verse)
    song.extend(verse)
    chorus[6] = chorusScale[1];
    song.extend(chorus)
    chorus[6] = chorusScale[2];
    song.extend(chorus)
    song.extend(verse)
    song.extend(verse)
    chorus[6] = chorusScale[1];
    song.extend(chorus)
    chorus[6] = chorusScale[0];
    song.extend(chorus)
    return song

def generateStochasticSongMajor():
    verseScale = [0, 2, 4, 5 ]
    chorusScale = [0, 2, 4, 5, 7, -1, 9]
    return generateStochasticSong(verseScale, chorusScale)

def generateStochasticSongMinor():
    verseScale = [-3, -1, 0, 2 ]
    chorusScale = [-3, -1, 0, 2, 4, 7, 5 ]
    return generateStochasticSong(verseScale, chorusScale)

def generateStochasticSongBlues():
    verseScale = [0, 3, 5, 6];
    chorusScale = [0, 3, 5, 6, 7, 10];
    return generateStochasticSong(verseScale, chorusScale)
    

#
# Parse command line arguments
#

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("songname", help="name of the song")
    parser.add_argument("lyricsfile", type=argparse.FileType('r'), help="name of the lyrics file")
    parser.add_argument("scale", nargs='?', default='major', help="'major', 'minor', or 'blues', default is 'major'")
    args = parser.parse_args()

    generateSong = None
    if args.scale == 'major':
        generateSong = generateStochasticSongMajor
    elif args.scale == 'minor':
        generateSong = generateStochasticSongMinor
    elif args.scale == 'blues':
        generateSong = generateStochasticSongBlues
    else:
        sys.stderr.write("Invalid scale '%s'\n" % (args.scale))
        sys.exit(1)

    songnameSyllables = breakIntoSyllables(args.songname)
    lyricSyllables = breakIntoSyllables(args.lyricsfile.read())
    verse1 = lyricSyllables[0:26]
    verse2 = lyricSyllables[26:52]
    chorus = songnameSyllables + lyricSyllables[-7+len(songnameSyllables):]
    lyrics = verse1 + chorus + chorus + verse2 + chorus + chorus
    
#    print "songnameSyllables", songnameSyllables
#    print "lyricSyllables", lyricSyllables
#    print "verse1", verse1
#    print "verse2", verse2
#    print "chorus", chorus

    
    song = generateSong()
    root = generateXML(song)
    addLyrics(root, lyrics)

    #
    # Output XML
    #

#    print """<?xml version="1.0" encoding='UTF-8' standalone='no' ?>
#<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">"""
    print ET.tostring(root, encoding='UTF-8')

