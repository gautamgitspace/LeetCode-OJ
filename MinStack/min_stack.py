#!/usr/bin/env python

"""
using just one list that stores elements as they are pushed
in the format [x, y] where x is the element being pushed and
y is the current minimum value
"""
class MinStack(object):

    def __init__(self):
        self.s = [(-1, float(inf)]

    def push(self, x):
        self.s.append(x, min(x, self.s[-1][1]))

    def pop(self):
        if len(self.s) > 1: self.s.pop()

    def top(self):
        if len(self.s) == 1: return None
        return self.s[-1][0]

    def getMin(self):
        return self.s[-1][1]
