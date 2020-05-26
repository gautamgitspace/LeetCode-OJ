"""
same approach as LC 325 where we find the max cont. array
whose sum equals k. here, replace all 0's with -1's and
imagine k to be 0

so [1,0,1,0] becomes [1,-1,1,-1]
and cont. arrays that have k as 0 are [1,-1] and [1,-1,1,-1]
so we return 4, max of the two.

in case of [1,0,1] becomes [1,-1,1] and we return [1,-1] or [-1,1]
both are of length 2
"""
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # make all zeroes ones
        for i in range(len(nums)):
            if nums[i] == 0: nums[i] = -1
        d = {}
        d [0] = -1
        pre_sum, max_len = 0, 0
        for i in range(len(nums)):
            pre_sum += nums[i]
            if pre_sum in d:
                max_len = max(max_len, i - d[pre_sum])
            else:
                d[pre_sum] = i
        return max_len
