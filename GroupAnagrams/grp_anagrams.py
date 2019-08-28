#!/usr/bin/env python

from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        """
        can't use list as a dict key as dict
        keys need to be hashable (immutable)
        hence use a tuple instead.

        Why sort? so that key is same for all
        anagrams
        """
        anagrams = defaultdict(list)
        for str in strs:
            anagrams[tuple(sorted(str))].append(str)
        return anagrams.values()
