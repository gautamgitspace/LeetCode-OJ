class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        [0,1,2,4,5,6,7] = Original

        [6,7,0,1,2,4,5] = R1
               ^     ^
        [4,5,6,7,0,1,2] = R2
               ^     ^
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right)//2
            if nums[mid] > nums[right]:
                # minimum must be to the right of the middle
                # cause in normal scenario, mid must be less
                # than last element of the sorted array
                # so set the start bounds as mid + 1
                left = mid + 1
            else:
                # NORMAL ASCENDING FLOW
                # minimum must be to the left of the middle
                # or might be middle as well. we set the
                # end bound by restricting right to mid
                right = mid
        return nums[left]
