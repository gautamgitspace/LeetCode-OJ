class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        same as 3sum basic problem we use 3 pointers - i, l and r
        in addition we need to keep track of closest sum. Now
        closest sum to target will be the smaller value between
        (closest_sum - target) and (curr_sum - target) so whenever
        (curr_sum - target) is lt the (closest_sum - target), we
        know that we have a new closest_sum, so we update it.

        when l < r expires we increment i and have new l and r.
        we again do the same process and track closest_sum.
        once we have checked all elements, we return closest_sum
        """
        nums.sort()
        closest_sum = float("inf")
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if curr_sum == target:
                    return curr_sum
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum
                if curr_sum < target:
                    l += 1
                else:
                    r -= 1
        return closest_sum
