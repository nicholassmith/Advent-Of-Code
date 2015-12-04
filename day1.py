#!/usr/bin/python

import sys, argparse

parser = argparse.ArgumentParser(description='What floor is the right floor')
parser.add_argument('-i', '--input', help='Input of instructions', required=True)
args = parser.parse_args()

inputFile = open(args.input, 'rb')

floor = 0

inputString = inputFile.read()

for x in range(len(inputString)):
	if(inputString[x] == "("):
		floor = floor + 1
	elif(inputString[x] == ")"):
		floor = floor - 1

	if(floor == -1):
		print "Basement at", x

print "Santa should goto floor", floor