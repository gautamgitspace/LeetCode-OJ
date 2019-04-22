#!/usr/bin/python
"""
do a binary search to find the element iff it exists - O(logn)
if it doesn't, just iterate through the array using another
routine and keep incrementing index until you hit the target - O(n)
Total - O(logn) + O(n)

"""
class Solution(object):
    def searchInsertIndex(self, nums, target):
        index = 0
        if target > nums[-1]:
            return len(nums)
        for items in nums:
            if target > items:
                index += 1
                continue
            else:
                return index

    def searchInsert(self, nums, target):

        if not nums:
            return -1

        l = 0
        r = len(nums) - 1

        while (l <= r):
            mid = l+ (r-l)/2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1


if __name__ == "__main__":
    sol = Solution()
    nums = [2,4,9,10,15]
    target = 15
    result = sol.searchInsert(nums, target)
    if  result is None:
        print sol.searchInsertIndex(nums, target)
    else:
        print result
