#!/usr/bin/python

import sys, argparse

start = [1,1,1,3,1,2,2,1,1,3]
next = []

for x in range(40):
	numList = start
	
	numGroup = [numList[0]]

	i = 1
	while i < len(numList):
		if(numList[i] in numGroup):
			numGroup.append(numList[i])
		else:
			next.append(len(numGroup))
			next.append(numGroup[0])
			numGroup = []
			numGroup.append(numList[i])
		i += 1

	next.append(len(numGroup))
	next.append(numGroup[0])
	
	start = next
	next = []


print len(start)