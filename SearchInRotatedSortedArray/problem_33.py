#!/usr/bin/python
class Solution(object):
    def n_search(self, nums, target):
        for i, item in enumerate(nums):
            if target == item:
                return i
            else:
                continue
        return -1
    def log_n_search(self, nums, target):
        """
        [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]
        here pivot point is element 2 (idx 2) after
        which the flip happens.

        [SOL 0] - Good time complexity
        If we are able to find out the pivot point, we can have
        two sorted arrays and do a binary search in O(logn)

        [SOL 1] - Bad time complexity
        No use doing a sort as that will be another expensive
        operation of O(nlogn). No use doing reverse and other
        stuff either.
        """
        i = 1
        length = len(nums)
        flip = 0
        while i < length:
            if nums[i] > nums[i-1]:
                i += 1
                continue
            else:
                flip = i
                break
        left = nums[flip:]
        right = nums[:flip]

        low = int(left[0])
        high = int(right[-1])
        mid = (low + high)/2

        #do a binary search on dummy and nums now
        if target > mid:
            if target in right:
                return nums.index(target)
            else:
                return -1
        else:
            if target in left:
                return nums.index(target)
            else:
                return -1


nums = [4,5,6,7,0,1,2]
sol = Solution()
print sol.n_search(nums, 7)
print sol.n_search(nums, 14)
print sol.log_n_search(nums, 2)
print sol.log_n_search(nums, 14)
