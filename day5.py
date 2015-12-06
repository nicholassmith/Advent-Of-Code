#!/usr/bin/python

import sys, argparse, re

parser = argparse.ArgumentParser(description='Nice and naughty strings.')
parser.add_argument('-i', '--input', help='Input of strings.', required=True)
args = parser.parse_args()

inputFile = open(args.input, 'rb')

niceStrings = 0

for line in inputFile:
	fileLine = line.strip()
	naughtyGroups = re.compile('(ab|cd|pq|xy)')
	if(naughtyGroups.search(fileLine)) is None:
		vowels = re.compile('[aeiou]')
		matches = re.findall(vowels, fileLine)
		if(len(matches) >= 3):
			n = 2
			print fileLine.strip()
			for i in range(0, len(fileLine.strip())):
				subset = fileLine[i:i+n]
				print subset
				if(subset.endswith(subset[0]) and len(subset) == 2):
					niceStrings = niceStrings + 1
					break
			
print niceStrings