"""
RULES:
    - Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    - Any right parenthesis ')' must have a corresponding left parenthesis '('.
    - Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    - '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
    - An empty string is also valid.

"""class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, star = [], []
        for i in range (len(s)):
            if s[i] == '(':
                left.append(i)
            elif s[i] == '*':
                star.append(i)
            else:
                # we have encountered a closing bracket
                # gotta pop now, from left first if it
                # has something, otherwise pop from star
                if len(left) == 0 and len(star) == 0: return False
                if len(left) != 0:
                    left.pop()
                else:
                    star.pop()
        # STORY TIME
        # now for cases we do not encounter a closing bracket at all. such cases
        # won't be taken care by the three conditional statements above but our
        # stacks contain some stuff at this point, using which we gotta decide
        # the validity of the string. 
        #
        # So we pop and compare the indices. Indices
        # stored in left can never be greater than that stored in start. WHY?
        #
        # take a case **((. In this left will have 2,3 and star will have 0,1. 
        # on popping se see that left.pop() > star.pop() and we know that its not
        # valid. as it can result in (( or ))(( or ((((. all of which are not
        # valid.
        while(len(left) != 0 and len(star) != 0):
            if(left.pop() > star.pop()):
                return False
        # finally, a correctly balanced string would result in empty left stack
        return len(left) == 0
