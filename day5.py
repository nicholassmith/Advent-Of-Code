#!/usr/bin/python

import sys, argparse, re
from collections import Counter

parser = argparse.ArgumentParser(description='Nice and naughty strings.')
parser.add_argument('-i', '--input', help='Input of strings.', required=True)
args = parser.parse_args()

inputFile = open(args.input, 'rb')

niceStrings = []

partialStrings = []

for line in inputFile:
	fileLine = line.strip()

	n = 3
	for i in range(0, len(fileLine.strip())):
		subset = fileLine[i:i+n]
		if(subset.endswith(subset[0]) and len(subset) == 3):
			partialStrings.append(fileLine)
			break

print 'num partials', len(partialStrings)

for string in partialStrings:
	n = 2
	doubleChars = []
	for i in range(0, len(string)):
		doubleChars.append(string[i:i+n])

	dupes = [k for k,v in Counter(doubleChars).items() if v>1]
	if(dupes):
		print "our dupes", dupes
		index = doubleChars.index(dupes[0])
		print index
		if(doubleChars[index] == doubleChars[index+1]):
			print "bad string is:", string
			print "true overlap"
		else:
			print "nice string is:", string
			niceStrings.append(string)
				
			
print len(niceStrings)