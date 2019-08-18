#!/usr/bin/python

"""
we have to find the first character that does not repeat
down the line in the string.

in 'leetcode' non repeating chars are: l,t,c,o,d and l
is the first of them. so we return the index of l

in 'loveleetcode' non repeating chars are: v,t,c,d and
v is first of them.. so we return the index of v

APPROCAH: all we need to do is keep count of all in a
counter. then traverse the string and keep checking the
count of chars and return the very first who's count is 1
"""
import collections
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)
        print count
        for index, char in enumerate(s):
            if count[char] == 1:
                return index
        return -1
