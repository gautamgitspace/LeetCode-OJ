"""

    1 0 2 2 1 0
    ^         ^
    L         H
    M

    Mid != 0 || 2
    Mid++

    1 0 2 2 1 0
    ^ ^       ^
    L M       H

    Mid == 0
    Swap Low and Mid
    Mid++
    Low++

    0 1 2 2 1 0
      ^ ^     ^
      L M     H

    Mid == 2
    Swap High and Mid
    High--

    0 1 0 2 1 2
      ^ ^   ^
      L M   H

    Mid == 0
    Swap Low and Mid
    Mid++
    Low++

    0 0 1 2 1 2
        ^ ^ ^
        L M H

    Mid == 2
    Swap High and Mid
    High--

    0 0 1 1 2 2
        ^ ^
        L M
          H

    Mid <= High is our exit case


"""
class Solution(object):
    def __swap(self, l, i, j):
        tmp = l[i]
        l[i] = l[j]
        l[j] = tmp

    def sortColors(self, nums):
        low, mid, high = 0, 0, len(nums)-1
        # exit condition
        while mid <= high:
            # mid is taking low's sapce.
            # SWAP mid and low, increment mid and low
            if nums[mid] == 0:
                self.__swap(nums, mid, low)
                low += 1
                mid += 1
            # mid is taking no ones, place. Move mid
            # so that it does take someone's place
            elif nums[mid] == 1:
                mid += 1
            # mid is taking high's place.
            # SWAP mid and high, decrement high
            elif nums[mid] == 2:
                self.__swap(nums, mid, high)
                high -= 1
