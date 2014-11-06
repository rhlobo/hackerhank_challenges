#!/usr/bin/env python


import tester
tester.configure()


'''
https://www.hackerrank.com/challenges/utopian-tree
'''


for _ in xrange(int(raw_input())):
    cycles = int(raw_input())
    total = 1
    for c in xrange(1, cycles + 1):
        total = total + 1 if c % 2 == 0 else total * 2
    print total
