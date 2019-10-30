class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        d = {}

        # populate map for target string
        for char in p:
            d[char] = d.get(char, 0) + 1

        """
        d =  {
             'a': 1 0 -1 -2 -1 0
             'c': 1 0 1 0
             'b': 1 0 -1 -2 -1 0
             }

             counter : 3 2 1 0 1 0 1
        """

        counter = len(d)
        begin, end = 0, 0

        # outer loop scanning source till we die
        while end < len(s):
            # EXPANSION OF WINDOW
            # pick one char at a time from source,
            # check if its in d, if it is, decrement
            # its count, when count for a char reaches
            # 0, decrement the counter, when counter
            # becomes 0, we do our next magic. if its
            # not in d, just move ahead by incrementing
            # end ptr
            c = s[end]
            if c in d:
                d[c] = d.get(c) - 1
                if d[c] == 0:
                    counter -= 1
            end += 1

            # we will reach here when all keys in the will be
            # exhausted i.e. values for keys will be lt 0

            # magic i.e CONTRACTION OF WINDOW
            while counter == 0:
                # while counter remains 0, we are gonna do this stuff
                # counter will only increment from 0 to 1 if count of
                # the temp_c char (or char at the begin ptr) is +ve
                # +ve means we have fresh keys to exhaust now (WIN EXP)
                # The moment it becomes +ve, we bail out of this while
                # and continue doing the stuff we were doing above
                temp_c = s[begin]
                if temp_c in d:
                    d[temp_c] = d.get(temp_c) + 1
                    if d[temp_c] > 0:
                        counter += 1
                # append the index of onset of the anagram
                # only when (end ptr - begin ptr) == len(p)
                # as anagrams are same size
                if end - begin == len(p):
                    res.append(begin)
                # once appended, increment the begin ptr
                begin += 1
        return res
