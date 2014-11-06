#!/usr/bin/env python


import tester
tester.configure()


'''
https://www.hackerrank.com/challenges/cut-the-sticks
'''

_ = raw_input()
length = [int(x) for x in raw_input().split()]

while len(length) >= 1:
    print len(length)
    smallest = min(length)
    length = [x - smallest for x in length if x - smallest > 0]
