#!/usr/bin/env python


import tester
tester.configure()


'''
https://www.hackerrank.com/challenges/gem-stones
'''


n = int(raw_input())

common = set(raw_input())
for i in xrange(1, n):
    common &= set(raw_input())

print len(common)
