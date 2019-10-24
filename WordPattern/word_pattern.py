class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool

        Input: pattern = "abba", str = "dog cat cat dog"
        Output: true

        Input:pattern = "abba", str = "dog cat cat fish"
        Output: false

        Input: pattern = "aaaa", str = "dog cat cat dog"
        Output: false

        Input: pattern = "abba", str = "dog dog dog dog"
        Output: false
        """
        # clear outlier
        if len(list(pattern)) != len(str.split(" ")):
            return False
        # outlier for cases like second example
        if len(set(list(pattern))) != len(set(str.split(" "))):
            return False
        # for all other cases maintain a map
        d = {}
        for i, char in enumerate(list(pattern)):
            if char not in d:
                d[char] = str.split(" ")[i]
            else:
                if d[char] != str.split(" ")[i]:
                    return False
        return True
