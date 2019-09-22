#!/usr/bin/env python

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        max = A[0]
        for i in range(1, len(A)):
            if A[i] > max:
                max = A[i]
            else:
                return i-1
    def or_maybe_just(self, A):
        for i in range(0, len(A)):
            if A[i+1] > A[i]:
                continue
            else:
                return i
