class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """

        """
        key is to store how many times (a+b) appears
        so the table will store what (a+b) is and the
        number of times these (a+b) sums appear.

        Then we increment the count every time -(c+d)
        appears in the table. as -(c+d) makes (a+b) null
        i.e. (a+b) = (c+d)
        """
        table = {}
        count = 0

        for a in A:
            for b in B:
                table[a + b] = table.get((a+b), 0) + 1

        for c in C:
            for d in D:
                if (-(c+d)) in table:
                    count += table[-(c+d)]
        return count
