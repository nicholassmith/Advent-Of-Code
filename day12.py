#!/usr/bin/python

import sys, argparse
import json
import itertools

parser = argparse.ArgumentParser(description='AbacusFramework')
parser.add_argument('-i', '--input', help='Input of instructions', required=True)
args = parser.parse_args()

inputFile = open(args.input, 'rb')

jsonData = json.loads(inputFile.read())

def parse_json(obj):
	if isinstance(obj, int):
		return obj
	elif isinstance(obj, str):
		return 0
	elif isinstance(obj, list):
		return sum(map(parse_json, obj))
	elif isinstance(obj, dict):
		return sum(map(parse_json, obj.values()))
	else:
		return 0



print 'total', parse_json(jsonData)