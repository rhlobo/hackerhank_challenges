#!/usr/bin/env python


import tester
tester.configure()


'''
https://www.hackerrank.com/challenges/halloween-party
'''


def solve(k):
    rows = k / 2
    cols = k - rows
    return rows * cols


T = int(raw_input())
for i in xrange(T):
    print solve(int(raw_input()))
