#!/usr/bin/env python


import tester
tester.configure()


'''
https://www.hackerrank.com/challenges/acm-icpc-team
'''


import operator
import itertools


N, M = [int(x) for x in raw_input().split()]
t = [[int(x) for x in raw_input()] for _ in xrange(N)]

biggest, count = 0, 0
for a, b in itertools.combinations(range(N), 2):
    total = sum(map(operator.or_, t[a], t[b]))
    if total > biggest:
        biggest, count = total, 1
    elif total == biggest:
        count += 1

print biggest
print count
