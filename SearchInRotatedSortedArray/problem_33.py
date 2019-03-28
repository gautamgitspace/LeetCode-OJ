#!/usr/bin/python
class Solution(object):
    def n_search(self, nums, target):
        """
        time complexity - Bad: O(n)
        list.index will O(n) as well
        """
        for i, item in enumerate(nums):
            if target == item:
                return i
            else:
                continue
        return -1

    def log_n_search_flex(self, nums, target):
        """
        time complexity - Good: O(logn)
        leverages binary search

        problem #81
        takes care of duplicate entries but worst case time complexity
         for such lists for eg. [1,1,1,1,1,2,2,3] is O(n)

        if you plan to remove the dups first, you'll end up Using
        extra structure and also adding O(n) time to your approach
        """
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) / 2
            if target == nums[mid]:
                return mid

            # normal ascending flow:
            if nums[low] <= nums[mid]:
                # target lies between low and mid - high becomes left of mid
                # othwewise low becomes right of mid
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # target lies between mid and high - low becomes right of mid
                # otherwise high becomes left of mid
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1


nums = [4,1,2,3]
sol = Solution()
#print sol.n_search(nums, 5)
print nums
print "target resides at idx " + str(sol.log_n_search_flex(nums, 1))
