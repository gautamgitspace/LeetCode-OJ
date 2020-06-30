class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        running_sum = []
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            running_sum.append(curr_sum)
        return running_sum
