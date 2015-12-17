#!/usr/bin/python

import sys, argparse
from itertools import permutations

parser = argparse.ArgumentParser(description='All In A Single Night')
parser.add_argument('-i', '--input', help='Input of instructions', required=True)
args = parser.parse_args()

inputFile = open(args.input, 'rb')

people = set()
graph = {}

for line in inputFile:
	(p1,_,operator,value,_,_,_,_,_,_,p2) = line.strip().split(' ')

	p1 = p1.replace('.', '')
	p2 = p2.replace('.', '')

	people.add(p1)
	people.add(p2)

	if(operator == 'lose'):
		value = '-' + value

	graph[p1, p2] = int(value)

happiness = []

for perm in permutations(people):
	happydex = 0
	for i in range(len(perm)):
		happydex += graph[perm[i],perm[i-1]]
		happydex += graph[perm[i-1],perm[i]]
	happiness.append(happydex)

print max(happiness)