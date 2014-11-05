#!/usr/bin/env python


import tester
tester.configure()


'''
https://www.hackerrank.com/challenges/game-of-thrones
'''


from collections import Counter


def count_odd(l):
    return (l[0] % 2) + count_odd(l[1:]) if l else 0

string = raw_input()
print "NO" if count_odd(Counter(string).values()) > 1 else "YES"
