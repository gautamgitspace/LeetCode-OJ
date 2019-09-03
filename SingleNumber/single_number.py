"""
O(n) extra space:
    - count sort and return index of element with val 1
    - dict and return key with val of 1
    - use set keep adding if not seen, keep removing if seen. return set
O(n) no extra space:
    - xor elements with each other. property of XOR: A^A = 0, A^B^A = B
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        return res
