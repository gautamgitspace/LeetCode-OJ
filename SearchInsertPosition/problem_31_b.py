#!/usr/bin/python
"""
adoption of binary search but we do not return mid here.
we return low which is also equal to high+1
O(logn) for binary search
"""
class Solution(object):
    def searchInsert(self, nums, target):
        if not nums:
            return -1
        l = 0
        r = len(nums) - 1

        while (l <= r):
            mid = l+ (r-l)/2
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return l


if __name__ == "__main__":
    sol = Solution()
    nums = [2,4,9,10,15]
    target = 11
    result = sol.searchInsert(nums, target)
    print result
