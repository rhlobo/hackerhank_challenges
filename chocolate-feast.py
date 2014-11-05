#!/usr/bin/env python


import tester
tester.configure()


'''
https://www.hackerrank.com/challenges/chocolate-feast
'''


for _ in xrange(int(raw_input())):
    N, C, M = [int(x) for x in raw_input().split(' ')]

    answer = N / C

    wrapper = answer
    while wrapper >= M:
        bonus = wrapper / M
        answer += bonus
        wrapper = (wrapper % M) + bonus

    print answer
