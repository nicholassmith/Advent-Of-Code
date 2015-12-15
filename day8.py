#!/usr/bin/python

import sys, argparse, itertools

parser = argparse.ArgumentParser(description='Matchsticks')
parser.add_argument('-i', '--input', help='Input of instructions', required=True)
args = parser.parse_args()

inputFile = open(args.input, 'rb')

codeChars = 0
stringChars = 0
encodedChars = 0 

for line in inputFile:
	codeChars = codeChars + len(line.strip())
	print line.strip().encode('string_escape')
	stringChars = stringChars + len(eval(line.strip()))
	encodedChars = encodedChars + 2 + line.count('\\') + line.count('"') + len(line.strip())


print 'codeChars count', codeChars
print 'stringChars count', stringChars
print 'encodedChars count', encodedChars
print 'final pt1: ', codeChars - stringChars
print 'final pt2:', encodedChars - codeChars