#!/usr/bin/python

import sys
import argparse
import subprocess
import re

def requestFromWebsite(infile, outfile, spkrlang, spkr, synalpha, vibpower, f0shift):
    htmlOutput = subprocess.check_output([ 'curl', '-v', '-F', 'LANG=jp', '-F', 'SPKR_LANG='+spkrlang, '-F', 'SPKR='+spkr, '-F', 'SYNALPHA='+synalpha, '-F', 'VIBPOWER='+vibpower, '-F', 'F0SHIFT='+f0shift, '-F', 'SYNSRC=@' + infile, 'http://sinsy.sp.nitech.ac.jp/index.php' ])

    m = re.search('\.\/(temp\/[0-9_]+\.wav)', htmlOutput)
    wavFile = m.group(0)

    subprocess.check_call(['curl', '-o', outfile, 'http://sinsy.sp.nitech.ac.jp/' + wavFile])

#
# Parse command line arguments
#

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", help="name of the input xml file")
    parser.add_argument("outfile", help="name of the output wave file")
    parser.add_argument('--spkr', default='4', help="speaker, default is 4, Japanese voices: 0=Yoko  1=Xiang-Ling  2=Namine Ritsu S  3=undefined  7=Yoko DNN, English voices: 4=Xiang-Ling (Female)  5=Matsuo-P (Male), Mandarin voices: 6=Xiang-Ling")
    parser.add_argument('--synalpha', default='0.55', help="synalpha, default is 0.55 (-0.8 to 0.8)")
    parser.add_argument('--vibpower', default='1', help="vibpower, default is 1 (0.0 to 2.0)")
    parser.add_argument('--f0shift', default='0', help="f0shift, default is 0 (-24 to 23)")

    args = parser.parse_args()

    spkrlang = 'english'
    if args.spkr == '0':
        spkrlang = 'japanese'
    elif args.spkr == '1':
        spkrlang = 'japanese'
    elif args.spkr == '2':
        spkrlang = 'japanese'
    elif args.spkr == '3':
        spkrlang = 'japanese'
    elif args.spkr == '7':
        spkrlang = 'japanese'
    elif args.spkr == '4':
        spkrlang = 'english'
    elif args.spkr == '5':
        spkrlang = 'english'
    elif args.spkr == '6':
        spkrlang = 'mandarin'
    else:
        sys.exit("Unknown spkr: " + args.spkr)

    if float(args.synalpha) < -0.8 or float(args.synalpha) > 0.8:
        sys.exit("The parameter synalpha should be between -0.8 and 0.8")
    if float(args.vibpower) < 0.0 or float(args.vibpower) > 2.0:
        sys.exit("The parameter vibpower should be between 0.0 and 2.0")
    if int(args.f0shift) < -24 or int(args.f0shift) > 23:
        sys.exit("The parameter f0shift should be between -24 and 23")

    requestFromWebsite(args.infile, args.outfile, spkrlang, args.spkr, args.synalpha, args.vibpower, args.f0shift)
