#!/usr/bin/python

import sys, argparse, hashlib

parser = argparse.ArgumentParser(description='Advent coins')
parser.add_argument('-i', '--input', help='Input string', required=True)
args = parser.parse_args()

x = 0
matchFound = False

while(matchFound == False):
	stringToHash = args.input + str(x)

	hashedString = hashlib.md5(stringToHash).hexdigest()
	if(hashedString[:5] == '00000'):
		matchFound = True
	else:
		x = x + 1

print "match found at x", x