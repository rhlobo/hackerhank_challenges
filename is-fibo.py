#!/usr/bin/env python


import tester
tester.configure()


'''
https://www.hackerrank.com/challenges/is-fibo
'''


import math


def is_fibo(n):
    c = 5 * (n ** 2)
    return is_psqrt(c + 4) or is_psqrt(c - 4)


def is_psqrt(n):
    isqrt = int(math.sqrt(n) + 0.5)
    return (isqrt ** 2) == n


T = int(raw_input())
for _ in xrange(T):
    N = int(raw_input())
    print 'IsFibo' if is_fibo(N) else 'IsNotFibo'
