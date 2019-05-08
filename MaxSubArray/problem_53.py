#!/usr/bin/python

"""
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum
and return its sum.

KEY - This is the famous Maximum subarray problem. Maintain two max pointers.

max_so_far: will be updated with every iteration (beginning with 0th element +
1st element compared to 1st element and so on...)

max_return: will be updated with every iteration and will be just the higher of
the previous max_return and the new max_so_far computed
"""

class Solution:
    def max_sub_array(self, arr):
        max_return = arr[0]
        max_so_far = arr[0]
        for i in range (1, len(arr)):
            print "evaluating max of: " + str(max_so_far + int(arr[i])) + " and " +str(int(arr[i]))
            max_so_far = max(max_so_far + int(arr[i]), int(arr[i]))
            print "max_so_far: " + str(max_so_far)
            max_return = max(max_return, max_so_far)
            print "max_return: " + str(max_return)
        return max_return

if __name__ == "__main__":
    sol = Solution()
    input = [-2,1,-3,4,-1,2,1,-5,4]
    print sol.max_sub_array(input)
