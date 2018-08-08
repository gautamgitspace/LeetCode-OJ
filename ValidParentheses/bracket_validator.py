#!/usr/bin/python

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        set1, set2 = "[{(", "]})"
        for c in s:
            if c in set1:
                stack.append(c)
            elif c in set2:
                if len(stack) == 0:
                    return False
                else:
                    stack_top = stack.pop()
                    balancing_bracket = set1[set2.index(c)]
                    if stack_top != balancing_bracket:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False
