class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(set(A)) == 1:
            return True
        dec, inc = False, False
        first = A[0]
        for item in A:
            if item == first:
                pass
            else:
                second = item

        if first < second:
            # increasing candidate
            for i in range(1, len(A)):
                if A[i-1] <= A[i]:
                    inc = True
                else:
                    # once wrong placeholder encountered, bail out
                    inc = False
                    break
        if second < first:
            # decreasing candidate
            for i in range(1, len(A)):
                if A[i-1] >= A[i]:
                    dec = True
                else:
                    dec = False
                    break
        if inc or dec:
            return True

"""
Below passes 323 / 366 test cases

but will fail [1,2,2,3] =)
        if A != sorted(A) or A != sorted(A, reverse=True):
            return False
        return True

"""

"""
but this will pass all cases =D

return sorted(A) in (A, A[::-1])
"""
