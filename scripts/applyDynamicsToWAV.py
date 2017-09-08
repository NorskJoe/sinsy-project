#!/usr/bin/python

import shutil
import wave
import sys
import argparse
import xml.etree.ElementTree as ET
import struct
import tempfile
import os

def extractDynamics(root):
    results = []
    lastMeasureNumber = 0
    lastDynamics = 'f'
    for a in root.findall('part'):
        for b in a.findall('measure'):
            measureNumber = int(b.attrib['number'])
            if measureNumber != lastMeasureNumber+1:
                return results
            lastMeasureNumber = measureNumber
            measureAttrs = {'crescendo':0, 'diminuendo':0}
            for c in b.findall('direction'):
                for d in c.findall('direction-type'):
                    for e in d.findall('dynamics'):
                        for f in list(e):
                            lastDynamics = f.tag
                    for e in d.findall('wedge'):
                        measureAttrs[e.attrib['type']] = 1
            measureAttrs['dynamics'] = lastDynamics
            measureAttrs['number'] = measureNumber
            results.append(measureAttrs)
    return results


#
# Parse command line arguments
#

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--inxml", type=argparse.FileType('rb'), default='-', help="name of the input xml file or stdin if not specified")
    parser.add_argument("--inwav", type=argparse.FileType('rb'), help="name of the input wav file", required=True)
    parser.add_argument("--outdynamics", help="name of output file for dynamics information for debugging (optional)")
    parser.add_argument("--outenvelope", help="name of output file for envelope information for debugging, the resulting file can be plotted using a program like gnuplot (optional)")
    parser.add_argument("--outwav", help="name of output file for wave or stdout if not specified")
    parser.add_argument("--pppp", default='0.1', help="value for dynamic pppp, between 0.0 and 1.0, default is 0.1")
    parser.add_argument("--ppp", default='0.1', help="value for dynamic ppp, between 0.0 and 1.0, default is 0.1")
    parser.add_argument("--pp", default='0.2', help="value for dynamic pp, between 0.0 and 1.0, default is 0.2")
    parser.add_argument("--p", default='0.3', help="value for dynamic p, between 0.0 and 1.0, default is 0.3")
    parser.add_argument("--mp", default='0.4', help="value for dynamic mp, between 0.0 and 1.0, default is 0.4")
    parser.add_argument("--mf", default='0.6', help="value for dynamic mf, between 0.0 and 1.0, default is 0.6")
    parser.add_argument("--f", default='0.8', help="value for dynamic f, between 0.0 and 1.0, default is 0.8")
    parser.add_argument("--ff", default='0.9', help="value for dynamic ff, between 0.0 and 1.0, default is 0.9")
    parser.add_argument("--fff", default='1.0', help="value for dynamic fff, between 0.0 and 1.0, default is 1.0")
    parser.add_argument("--ffff", default='1.0', help="value for dynamic ffff, between 0.0 and 1.0, default is 1.0")
    parser.add_argument("--sp", default='0.3', help="value for dynamic sp, between 0.0 and 1.0, default is 0.3")
    parser.add_argument("--sf", default='0.8', help="value for dynamic sf, between 0.0 and 1.0, default is 0.8")
    parser.add_argument("--smoothing", default='0.05', help="value for smoothing dynamic changes, represents time percentage of a measure, default is 0.05")
    parser.add_argument("--crescendo", default='0.15', help="change value for applying crescendo, default is 0.15")
    parser.add_argument("--diminuendo", default='-0.15', help="change value for applying diminuendo, should be negative, default is -0.15")
    args = parser.parse_args()

    dynamicsTable = {}
    dynamicsTable['pppp'] = float(args.pppp)
    dynamicsTable['ppp'] = float(args.ppp)
    dynamicsTable['pp'] = float(args.pp)
    dynamicsTable['p'] = float(args.p)
    dynamicsTable['mp'] = float(args.mp)
    dynamicsTable['mf'] = float(args.mf)
    dynamicsTable['f'] = float(args.f)
    dynamicsTable['ff'] = float(args.ff)
    dynamicsTable['fff'] = float(args.fff)
    dynamicsTable['ffff'] = float(args.ffff)
    dynamicsTable['sp'] = float(args.sp)
    dynamicsTable['sf'] = float(args.sf)

    #
    # Parse XML
    #

    root = ET.fromstring(args.inxml.read())

    inwav = wave.open(args.inwav)
    nchannels = inwav.getnchannels()
    sampwidth = inwav.getsampwidth()
    framerate = inwav.getframerate()
    nframes = inwav.getnframes()

    print >> sys.stderr, "nchannels", nchannels
    print >> sys.stderr, "sampwidth", sampwidth
    print >> sys.stderr, "framerate", framerate
    print >> sys.stderr, "nframes", nframes

    if nchannels != 1:
        sys.exit("Expecting only 1 channel in input wave file")

    if sampwidth != 2:
        sys.exit("Expecting 16-bit data in input wave file")

    allMeasures= extractDynamics(root)
    
    if args.outdynamics:
        with open(args.outdynamics, 'w') as outfile:
            for measure in allMeasures:
                outfile.write(str(measure) + "\n")

    numberOfMeasures = len(allMeasures)
    nframesPerMeasure = nframes / numberOfMeasures
    extraFrames = nframes % numberOfMeasures

    print >> sys.stderr, "numberOfMeasures:", numberOfMeasures
    print >> sys.stderr, "nframesPerMeasure", nframesPerMeasure
    print >> sys.stderr, "extraFrames", extraFrames

    envelope = []
    for measureIndex in range(0, numberOfMeasures):
        measure = allMeasures[measureIndex]
        nextMeasure = measure
        if measureIndex+1 < numberOfMeasures:
            nextMeasure = allMeasures[measureIndex+1]
        dynamics = measure['dynamics']
        nextDynamics = nextMeasure['dynamics']

        if measure['crescendo'] or measure['diminuendo']:
            crescendoOrDiminuendoValue = float(args.crescendo)
            if measure['diminuendo']:
                crescendoOrDiminuendoValue = float(args.diminuendo)
            nframesTransition = int(nframesPerMeasure*float(args.smoothing))
            nframesNormal = nframesPerMeasure - nframesTransition
            if measureIndex+1 == numberOfMeasures:
                nframesNormal = nframesPerMeasure
                nframesTransition = 0
            step = 0
            if nframesNormal:
                step = crescendoOrDiminuendoValue/float(nframesNormal)
            lastValue = dynamicsTable[dynamics]
            for i in range(0, nframesNormal):
                lastValue = dynamicsTable[dynamics]+step*float(i)
                envelope.append(lastValue)
            step = 0
            if nframesTransition:
                step = float(dynamicsTable[nextDynamics] - lastValue)/float(nframesTransition)
            for i in range(0, nframesTransition):
                envelope.append(lastValue+step*float(i))
        else:
            nframesTransition = int(nframesPerMeasure*float(args.smoothing))
            nframesNormal = nframesPerMeasure - nframesTransition
            step = (dynamicsTable[nextDynamics] - dynamicsTable[dynamics])/float(nframesTransition)
            for i in range(0, nframesNormal):
                envelope.append(dynamicsTable[dynamics])
            for i in range(0, nframesTransition):
                envelope.append(dynamicsTable[dynamics]+step*float(i))

    if extraFrames > 0:
        for i in range(0, extraFrames):
            envelope.append(envelope[-1])

    if args.outenvelope:
        with open(args.outenvelope, 'w') as outfile:
            for i in range(0, len(envelope)):
                outfile.write(str(i+1) + " " + str(envelope[i]) + "\n")

    outwavdata = []
    for i in range(0, nframes):
        waveData = inwav.readframes(1)
        data = struct.unpack("<h", waveData)
        value = int(float(int(data[0])) * envelope[i])
        outwavdata.append(struct.pack("h", value))

        
    temp = tempfile.NamedTemporaryFile(mode='wb', delete=False, dir='.')
    outwav = wave.open(temp)
    outwav.setnchannels(nchannels)
    outwav.setsampwidth(sampwidth)
    outwav.setframerate(framerate)
    outwav.setnframes(nframes)
    outwav.writeframes(''.join(outwavdata))
    outwav.close()
    temp.close()
    f = open(temp.name, "rb")
    fdata = f.read()
    f.close()
    os.unlink(temp.name)
    if args.outwav:
        with open(args.outwav, 'wb') as f:
            f.write(fdata)
    else:
        sys.stdout.write(fdata)


