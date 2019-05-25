#!?usr/bin/pyhon

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        container = []
        flag = True
        for char in s:
            if not char.isdigit():
                if char.isalpha():
                    container.append(char.lower())
            else:
                container.append(char)

        for items in container:
            if container.pop(-1) != items:
                flag = False
                break
            else:
                continue
        return flag
