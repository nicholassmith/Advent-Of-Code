#!/usr/bin/python

import sys, argparse, itertools

parser = argparse.ArgumentParser(description='Bobby Tables logic gates')
parser.add_argument('-i', '--input', help='Input of instructions', required=True)
args = parser.parse_args()

inputFile = open(args.input, 'rb')

codeChars = 0
stringChars = 0 

for line in inputFile:
	codeChars = codeChars + len(line.strip())
	stringChars = stringChars + len(eval(line.strip()))


print 'codeChars count', codeChars
print 'stringChars count', stringChars
print 'final: ', codeChars - stringChars