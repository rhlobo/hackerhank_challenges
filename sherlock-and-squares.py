#!/usr/bin/env python


import tester
tester.add_testcase('sherlock-and-squares_input-02.txt', 'sherlock-and-squares_output-02.txt')
tester.configure()


'''
Hackerhank > All Domains > Algorithms > Warmup > Sherlock and Squares
https://www.hackerrank.com/challenges/sherlock-and-squares
'''


import math


def is_square_int(x):
    '''
        Dummy solution.

        Finds the square root, rounds it to the nearest
        integer and squares it again, comparing it with
        the original number.

        0.5 is added before rounding since you can never
        depend on exact comparisons when dealing with
        floating point computations.

        Alternate solution could use newton's method to
        quickly zero in the nearest integer square root
        (lower or equal), then squaring for the comparison.
        '''
    sqrt = int(math.sqrt(x) + 0.5)
    return sqrt if sqrt ** 2 == x else None


def square_ints(a, b):
    for i in xrange(a, b + 1):
        isqrt = is_square_int(i)
        if isqrt is not None:
            break
    else:
        return 0

    count = 1
    while True:
        isqrt += 1
        if isqrt ** 2 > b:
            return count
        count += 1

T = int(raw_input())
for _ in xrange(T):
    a, b = [int(x) for x in raw_input().split()]
    print square_ints(a, b)
