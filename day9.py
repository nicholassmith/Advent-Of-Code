#!/usr/bin/python

import sys, argparse
from itertools import permutations

parser = argparse.ArgumentParser(description='All In A Single Night')
parser.add_argument('-i', '--input', help='Input of instructions', required=True)
args = parser.parse_args()

inputFile = open(args.input, 'rb')

places = set()
graph = {}

for line in inputFile:
	(source,_,destination,_,time) = line.split(' ')
	places.add(source)
	places.add(destination)

	graph[source, destination] = int(time)
	graph[destination, source] = int(time)

distances = []

for perm in permutations(places):
	distances.append(sum(map(lambda x, y: graph[x,y], perm[:-1], perm[1:])))

print min(distances)
print max(distances)