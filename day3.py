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
santaRoboMap = {}

santaX = 0
santaY = 0
roboX = 0
roboY = 0

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

x = 0
while(x < len(inputString)):
	if(inputString[x] == '^'):
		santaY = santaY + 1
	elif(inputString[x] == 'v'):
		santaY = santaY - 1
	elif(inputString[x] == '>'):
		santaX = santaX + 1
	elif(inputString[x] == '<'):
		santaX = santaX - 1

	santaRoboMap[santaY,santaX] = 1

	if(inputString[x+1] == '^'):
		roboY = roboY + 1
	elif(inputString[x+1] == 'v'):
		roboY = roboY - 1
	elif(inputString[x+1] == '>'):
		roboX = roboX + 1
	elif(inputString[x+1] == '<'):
		roboX = roboX - 1

	santaRoboMap[roboY,roboX] = 1

	x = x + 2


print "number of houses with at least 1 present: ", len(houseMap)
print "number of houses with at least 1 present with robo Santa: ", len(santaRoboMap)
