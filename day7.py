#!/usr/bin/python

import sys, argparse, itertools

parser = argparse.ArgumentParser(description='Bobby Tables logic gates')
parser.add_argument('-i', '--input', help='Input of instructions', required=True)
args = parser.parse_args()

inputFile = open(args.input, 'rb')

calc = dict()
results = dict()

for command in inputFile:
    (ops, res) = command.split('->')
    calc[res.strip()] = ops.strip().split(' ')

calc['b'] = '16076'

def calculate(name):
    try:
        return int(name)
    except ValueError:
        pass

    if name not in results:
        ops = calc[name]
        if len(ops) == 1:
            res = calculate(ops[0])
        else:
            op = ops[-2]
            if 'AND' in op:
              res = calculate(ops[0]) & calculate(ops[2])
            elif 'OR' in op:
              res = calculate(ops[0]) | calculate(ops[2])
            elif 'NOT' in op:
              res = ~calculate(ops[1]) & 0xffff
            elif 'RSHIFT' in op:
              res = calculate(ops[0]) >> calculate(ops[2])
            elif 'LSHIFT' in op:
              res = calculate(ops[0]) << calculate(ops[2])
        results[name] = res
    return results[name]

print "a: %d" % calculate('a')