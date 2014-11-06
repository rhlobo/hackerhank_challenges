#!/usr/bin/env python


import tester
tester.configure()


'''
https://www.hackerrank.com/challenges/sherlock-and-gcd
'''


import fractions


def has_subset(l):
    llen = len(l)

    for i in xrange(llen):
        if l[i] > 1:
            start = i
            break

    if llen - start < 2:
        return False

    for i in xrange(start + 1, llen):
        last = l[i-1]
        curr = l[i]
        if curr > last and fractions.gcd(last, curr) == 1:
            return True


T = int(raw_input())
for _ in xrange(T):
    N = int(raw_input())
    A = [int(x) for x in raw_input().split()]

    print 'YES' if has_subset(A) else 'NO'
