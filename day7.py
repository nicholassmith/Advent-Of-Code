#!/usr/bin/python

import sys, argparse, itertools

parser = argparse.ArgumentParser(description='Bobby Tables logic gates')
parser.add_argument('-i', '--input', help='Input of instructions', required=True)
args = parser.parse_args()

inputFile = open(args.input, 'rb')

wires = {}
oppers = {'AND', 'OR', 'NOT', 'LSHIFT', 'RSHIFT'}

def getWireValue(name):
	try:
		return int(name)
	except ValueError:
		pass

	if name in wires:
		return wires[name]
	else:
		wires[name] = 0
		return wires[name]

for line in inputFile:
	(chunks, resultWire) = line.strip().split('->')
	ops = chunks.split(' ')
	if ops[0] in oppers:
		if(ops[0] == 'NOT'):
			wires[resultWire] = ~getWireValue(ops[1])
	else:
		print ops[0], ops[2]
		if ops[1] == 'AND':
			print getWireValue(ops[0]) & getWireValue(ops[2])
			wires[resultWire] = getWireValue(ops[0]) & getWireValue(ops[2])
		elif ops[1] == 'OR':
			wires[resultWire] = getWireValue(ops[0]) | getWireValue(ops[2])
		elif ops[1] == 'LSHIFT':
			wires[resultWire] = getWireValue(ops[0]) << getWireValue(ops[2])
		elif ops[1] == 'RSHIFT':
			wires[resultWire] = getWireValue(ops[0]) >> getWireValue(ops[2])


print getWireValue('a')