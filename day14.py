#!/usr/bin/python

import sys, argparse
from itertools import permutations

parser = argparse.ArgumentParser(description='Reindeer Speed')
parser.add_argument('-i', '--input', help='Input of instructions', required=True)
args = parser.parse_args()

inputFile = open(args.input, 'rb')

reindeers = {}

def getDistance(reindeer, runTime):
	(speed, time, rest) = reindeer
	return speed * time * (runTime / (time + rest)) + speed * min(time, runTime % (time + rest))

for line in inputFile:
	(reindeer,_,_,speed,_,_,time,_,_,_,_,_,_,rest,_) = line.strip().split(' ')
	reindeers[reindeer] = (int(speed),int(time),int(rest))

maxDistance = 0

for reindeer in reindeers:
	rDist = getDistance(reindeers[reindeer], 2503)
	if maxDistance < rDist:
		maxDistance = rDist

print maxDistance