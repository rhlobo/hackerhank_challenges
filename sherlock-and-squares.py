#!/usr/bin/env python


import tester
tester.add_testcase('sherlock-and-squares_input-02.txt', 'sherlock-and-squares_output-02.txt')
tester.configure()


'''
Hackerhank > All Domains > Algorithms > Warmup > Sherlock and Squares
https://www.hackerrank.com/challenges/sherlock-and-squares
'''


import math


def is_square_int(x, newton_method=False):
    '''
    Finds the integer square root, squares it again,
    and compares it with the original number.
    '''
    isqrt = _isqrt_impl_b(x) if newton_method else _isqrt_impl_a(x)
    return isqrt if isqrt ** 2 == x else None


def _isqrt_impl_a(x):
    '''
    0.5 is added before rounding since you can never
    depend on exact comparisons when dealing with
    floating point computations. Faster due to
    `math.sqrt` optimization.
    '''
    return int(math.sqrt(x) + 0.5)


def _isqrt_impl_b(x):
    '''
    Uses newton's method to quickly zero in the nearest
    integer square root. The algorithm is implemented for
    theoretical reasons, but is actually slower.
    '''
    x0, n = x / 1.0, x
    while True:
        x1 = (x0 + (n / x0)) / 2
        if abs(x1 - x0) < 1:
            return int(x1)
        x0 = x1


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
