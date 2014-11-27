#!/usr/bin/env python


import tester
tester.configure()


'''
https://www.hackerrank.com/challenges/angry-children
'''


n = input()
k = input()
candies = [input() for _ in xrange(n)]
candies.sort()

print min([candies[i + k - 1] - candies[i] for i in xrange(n - k)])
