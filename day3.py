#!/usr/bin/python

import sys, argparse

parser = argparse.ArgumentParser(description='How many houses get presents')
parser.add_argument('-i', '--input', help='Input of instructions', required=True)
args = parser.parse_args()

inputFile = open(args.input, 'rb')

inputString = inputFile.read()

x = 0
y = 0

houseMap = {}

for char in inputString:
	if char == '^':
		y = y + 1
	elif char == 'v':
		y = y - 1
	elif char == '>':
		x = x + 1
	elif char == '<':
		x = x - 1

	houseMap[y,x] = 1

print "number of houses with at least 1 present: ", len(houseMap)
