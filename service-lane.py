#!/usr/bin/env python


import tester
tester.configure()


'''
https://www.hackerrank.com/challenges/service-lane
'''


def parse_ints(line):
    return [int(x) for x in line.split()]


_, t = parse_ints(raw_input())
width = parse_ints(raw_input())


for i in xrange(t):
    i, j = parse_ints(raw_input())
    print min(width[i:j+1])
