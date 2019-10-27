class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        run this for nums = [9, 7, 10, 1, 8, 9]

        we start with:      sub [inf, inf]
        traversing nums we have:
        
        i = 0       [9]     sub [9, inf]
        i = 1       [7]     sub [7, inf]
        i = 2       [10]    sub [7, 10]
        i = 3       [1]     sub [1, 10]
        i = 4       [8]     sub [1, 8]
        i = 5       [9]     => val > sub[1] so return True
        We're done here
        """
        sub  = [float("inf"), float("inf")]
        for i in range(len(nums)):
            if nums[i] <= sub[0]:
                sub[0] = nums[i]
            elif sub[0] <= nums[i] <= sub[1]:
                sub[1] = nums[i]
            else:
                return True
        return False
