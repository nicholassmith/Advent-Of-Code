#!/usr/bin/python

import sys, argparse, itertools

parser = argparse.ArgumentParser(description='How many houses get presents')
parser.add_argument('-i', '--input', help='Input of instructions', required=True)
args = parser.parse_args()

inputFile = open(args.input, 'rb')

lightMap = [[0 for i in range(1000)] for j in range(1000)]

for line in inputFile:
	tokens = line.strip().split(' ')
	if(tokens[0] == 'turn'):
		if(tokens[1] == 'on'):
			startVals = tokens[2].split(',')
			yStart = int(startVals[0])
			xStart = int(startVals[1])
			endVals = tokens[4].split(',')
			yEnd = int(endVals[0])
			xEnd = int(endVals[1])
			for j in range(xStart, xEnd+1):
				for i in range(yStart, yEnd+1):
					lightMap[j][i] = lightMap[j][i]+1
		elif(tokens[1] == 'off'):
			startVals = tokens[2].split(',')
			yStart = int(startVals[0])
			xStart = int(startVals[1])
			endVals = tokens[4].split(',')
			yEnd = int(endVals[0])
			xEnd = int(endVals[1])
			for j in range(xStart, xEnd+1):
				for i in range(yStart, yEnd+1):
					lightMap[j][i] = lightMap[j][i]-1
					if lightMap[j][i] < 0:
						lightMap[j][i] = 0
	elif(tokens[0] == 'toggle'):
		startVals = tokens[1].split(',')
		yStart = int(startVals[0])
		xStart = int(startVals[1])
		endVals = tokens[3].split(',')
		yEnd = int(endVals[0])
		xEnd = int(endVals[1])
		for j in range(xStart, xEnd+1):
				for i in range(yStart, yEnd+1):
					lightMap[j][i] = lightMap[j][i] + 2

flatMap = list(itertools.chain(*lightMap))

print sum(flatMap)

# print lightMap


