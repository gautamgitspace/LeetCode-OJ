class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        count, res = 0, ''
        for c in S:
            if c == ')':
                count -= 1
            if count != 0:
                res += c
            if c == '(':
                count += 1
        return res
