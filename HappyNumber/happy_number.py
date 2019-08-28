#!/usr/bin/env python

"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting
with any positive integer, replace the number by the sum of the squares
of its digits, and repeat the process until the number equals 1
(where it will stay), or it loops endlessly in a cycle which does not
include 1. Those numbers for which this process ends in 1 are happy numbers.

KEY is - 'or it loops endlessly in a cycle which does not include 1' How
would you make sure it does not endlessly be seen? or maybe the moment its
seen the second time
"""
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n != 1:
            n = sum (int(i)**2 for i in str(n))
            if n in seen:
                return False
            else:
                seen.add(n)
        return True
