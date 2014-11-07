#!/usr/bin/env python


import tester
tester.add_testcase('filling-jars_input07.txt', 'filling-jars_output07.txt')
tester.configure()


'''
https://www.hackerrank.com/challenges/filling-jars/
'''


def read_ints():
    return [int(x) for x in raw_input().split()]


N, M = read_ints()
total = 0


for _ in xrange(M):
    a, b, k = read_ints()
    total += (b - a + 1) * k


print total/N
