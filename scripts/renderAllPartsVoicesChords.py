#!/usr/bin/python

import re
import argparse
import xml.etree.ElementTree as ET

def extractPartVoiceChord(root):
    results = {}
    for a in root.findall('part'):
        for b in a.findall('measure'):
            voice = None
            for c in b.findall('note'):
                for d in c.findall('chord'):
                    if voice != None:
                        key = a.attrib['id'] + '-' + voice + '-chord'
                        results[key] = 1
                for d in c.findall('voice'):
                    voice = d.text
                    key = a.attrib['id'] + '-' + voice
                    results[key] = 1
    return sorted(results.keys())

def parsePartVoiceChordKey(key):
    tokens = key.split('-')
    results = {}
    if len(tokens) < 2:
        return None
    results['part'] = tokens[0]
    results['voice'] = tokens[1]
    if len(tokens) >= 3:
        results['chord'] = True
    else:
        results['chord'] = False
    return results

def asQuotedString(str):
    return '"' + re.sub('"', '\\"', str) + '"'

def generateShellScript(parts, xmlfile, outputdir):
    print "# Output directory:", outputdir
    print "mkdir %s" % (asQuotedString(outputdir))
    print "#"
    print "# Rendering for the following parts:"
    mixwavfile = asQuotedString(outputdir + '/mix.wav')
    normwavfile = asQuotedString(outputdir + '/norm.wav')
    reverbwavfile = asQuotedString(outputdir + '/reverb.wav')
    compandwavfile = asQuotedString(outputdir + '/compand.wav')
    outputwavfile = asQuotedString(outputdir + '/output.wav')
    allWavFiles = []
    for key in parts:
        elt = parsePartVoiceChordKey(key)
        print "#   ", elt
        inxmlfile = asQuotedString(xmlfile)
        tempxmlfile = asQuotedString(outputdir + '/' + key + '.xml')
        tempwavfile = asQuotedString(outputdir + '/' + key + '.wav')
        allWavFiles.append(tempwavfile)
        if elt['chord']:
            print "python keepPart.py %s %s | python useChordNotes.py >%s" % (
                inxmlfile,
                elt['part'],
                tempxmlfile
            )
        elif elt['voice'] != '1':
            print "python keepPart.py %s %s | python useVoice.py - %s >%s" % (
                inxmlfile,
                elt['part'],
                elt['voice'],
                tempxmlfile
            )

        else:
            print "python keepPart.py %s %s >%s" % (
                inxmlfile,
                elt['part'],
                tempxmlfile
            )
        print "python upload.py %s %s" % (tempxmlfile, tempwavfile)
    print "# Mix"
    print "sox -m %s %s" % (' '.join(allWavFiles), mixwavfile)
    print "sox %s %s gain -n" % (mixwavfile, normwavfile)
    print "sox %s %s reverb" % (normwavfile, reverbwavfile)
    print "python soxCompand.py %s %s" % (reverbwavfile, outputwavfile)
    

#
# Parse command line arguments
#

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("xmlfile", help="name of the xml file")
    parser.add_argument("outputdir", help="name of the directory to use for the temporary files and final WAV file")
    args = parser.parse_args()

    #
    # Parse XML
    #

    f = open(args.xmlfile, 'r')
    data = f.read()
    f.close()

    root = ET.fromstring(data)

    parts = extractPartVoiceChord(root)

    generateShellScript(parts, args.xmlfile, args.outputdir)
