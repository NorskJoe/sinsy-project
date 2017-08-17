#!/usr/bin/python

import subprocess
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", help="name of input file")
    parser.add_argument("outfile", help="name of output file")
    args = parser.parse_args()

    cmd = [ 'sox', args.infile, args.outfile, 'compand', '0.3,1', '6:-70,-60,-20', '-5', '-90', '0.2' ]
    subprocess.check_call(cmd)
