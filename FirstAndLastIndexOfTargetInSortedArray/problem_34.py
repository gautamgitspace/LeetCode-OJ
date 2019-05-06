#!/usr/bin/python
"""
PS - Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
must be done in runtime complexity: O(log n).
If not target not found, return [-1, -1].

KEY - the return low binary search solution (problem #35) will give the insert position. target+1 will be that position after
all the repetitions of the target in the sorted array.
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
    nums = [2,4,9,10,10,10,10,10,10,15]
    target = 17
    result = []
    first = sol.searchInsert(nums, target)
    """
    two conditions to be handled when 'first' is returned as DOES NOT EXIST:
    (a) the target given were to be inserted in the last of the array.
        In that case, searchInsert would return the len of nums. This cannot
        be caught by nums[first]!=target as this condition will overflow.
    (b) the target given were to be inserted somewhere in between.
        In that case, nums[first] should be equal to target.

    if any of the above two are not fulfilled, we gotta return [-1, -1]
    """
    if first == len(nums) or nums[first] != target:
        result.extend((-1, -1))
        print result
    else:
        last = sol.searchInsert(nums, target+1) - 1
        result.extend((first, last))
        print result
