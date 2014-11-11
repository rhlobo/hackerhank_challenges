#!/usr/bin/env python


import tester
tester.configure()


'''
https://www.hackerrank.com/challenges/manasa-and-stones
'''


def possibilities(n, a, b):
    result = set()
    for i in range(0, n):
        result.add((i * b) + ((n - i - 1) * a))
    return sorted(result)


T = int(raw_input())
for test in xrange(T):
    n = int(raw_input())
    a = int(raw_input())
    b = int(raw_input())
    print ' '.join(map(str, possibilities(n, a, b)))
