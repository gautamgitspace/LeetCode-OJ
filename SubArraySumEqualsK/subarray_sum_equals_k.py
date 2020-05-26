#!/usr/bin/env python
"""
Given an array of integers and an integer k, you need to find
the total number of continuous subarrays whose sum equals to k.
"""

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """
        THOUGHT PROCESS:
        this can be solved by running sum approach
        the keyword 'continuous' should trigger this

        say for array [3,2,5,3,2,4] and k = 10,
        running sum:  [3,5,10,13,15,19]

        now in the running sum array we notice that
        there are three stretches where k can be 10.

        These are: 3 -> 13, 5 -> 15 and also 0 -> 10
        the last case is special and comes when we have k
        in the running sum itself

        now we need to build a dict such that key is running
        sum element and value is the number of times that
        running sum element appears in the running sum array

        we start with d[0] = 1 for the special case of 0->10

        we keep on calculating running sum index by index and
        check if [running element - k] is present in the dict.
        If it is, we add 1 (or the val at that key per say) to
        count.

        Note that from previous discussion:
        we have established that [running element - k]
        is a stretch where k is 10

        sample d for [3,2,5,3,2,4]
        d {0 : 1, 3 : 1, 5 : 1, 10 : 1, 13 : 1, 15 : 1, 19 : 1}
                                   ^       ^       ^
                                 c = 1   c = 2   c = 3
        total count = 3
        """
        count = 0
        max = 0
        sums = 0
        d = dict()
        d[0] = 1

        for i in range(len(nums)):
            sums += nums[i]             # running sum element calc
            count += d.get(sums-k,0)    # check if [running element - k] exists in d
            d[sums] = d.get(sums,0) + 1 # add running sum element to d
            # print d
        return(count)
    """
    this is the second problem where we have to return the
    maximum length of the subarray that sums up to k.

    Here we store d[running sum] : index and we start with
    0 : -1 meaning that running sum of 0 is at index -1 (before 0)

    Then if running sum - k is found in dict,  we store the length
    of sub array in max. length will be given by current index -
    index stored in dict.

    if not found, we store the sum in d against its index or update
    it if it already exists

    """
    def max_sub_array_sum_equal_k(self, nums, k):
        d = {}
        d[0] = -1
        sums, maximum = 0, 0
        for i in range(len(nums)):
            sums += nums[i]
            if sums-k in d:
                # i = curr idx, d[sums-k] = previous stored idx
                maximum = max(maximum, i - d[sums-k])
            if sums not in d:
                d[sums] = i
        return maximum


if __name__ == "__main__":
    s = Solution()
    nums = [2,3,1,2,4,3]
    k = 7
    print s.subarraySum(nums, k)
    #print s.max_sub_array_sum_equal_k(nums, k)
