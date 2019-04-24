#!/usr/bin/python

"""
Useless question so smart way to tackle it
"""
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.rstrip(' ').split(' ')[-1])
