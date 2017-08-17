#!/usr/bin/python

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
    parser.add_argument('--spkrlang', default='english', help="speaker language, 'english', 'japanese', or 'mandarin'")
    parser.add_argument('--spkr', default='4', help="speaker, default is 4, Japanese voices: 0=Yoko 1=Xiang-Ling 2=Namine Ritsu S 3=undefined 7=Yoko DNN, English voices: 4=Xiang-Ling 5=Matsuo-P, Mandarin voices: 6=Xiang-Ling")
    parser.add_argument('--synalpha', default='0.55', help="synalpha, default is 0.55")
    parser.add_argument('--vibpower', default='1', help="vibpower, default is 1")
    parser.add_argument('--f0shift', default='0', help="f0shift, default is 0")

    args = parser.parse_args()

    requestFromWebsite(args.infile, args.outfile, args.spkrlang, args.spkr, args.synalpha, args.vibpower, args.f0shift)
