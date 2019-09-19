class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        r = nums[0]
        imax, imin = r, r

        for i in range(1, len(nums)):
            # for negatives, we do a swap as negative makes
            # big smaller and small bigger
            if nums[i] < 0:
                imax, imin = imin, imax
            # max or min product is either the number itself
            # or imax(the previous number) * the current number
            imax = max(nums[i], imax * nums[i])
            imin = min(nums[i], imin * nums[i])
            r = max(r, imax)
        return r
