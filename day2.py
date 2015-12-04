#!/usr/bin/python

import sys, argparse

parser = argparse.ArgumentParser(description='How much paper & ribbon is needed')
parser.add_argument('-i', '--input', help='Input of instructions', required=True)
args = parser.parse_args()

inputFile = open(args.input, 'rb')

totalPaper = 0
totalRibbon = 0

for line in inputFile:
	values = line.strip().split('x')
	length = int(values[0])
	width = int(values[1])
	height = int(values[2])

	lw = length * width
	wh = width * height
	hl = height * length

	per1 = length + length + width + width
	per2 = width + width + height + height
	per3 = height + height + length + length

	smallestSide = min([lw, wh, hl])

	smallestPer = min([per1, per2, per3])

	paperReq = smallestSide + (2*lw + 2*wh + 2*hl)

	totalPaper = totalPaper + paperReq

	presentRibbon = smallestPer + (length * width * height)

	totalRibbon = totalRibbon + presentRibbon



print "Total paper required is:", totalPaper
print "Total ribbon required is:", totalRibbon