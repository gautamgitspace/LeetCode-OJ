#!/usr/bin/python
class Sum:
    def three_sum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            """
            i = current number which will be used as a base for addition(target)
            l = ptr to track other numbers from the left (min)
            r = ptr to track other numbers from the right (max)
            If the number is the same as the number before, we have used it as target already so continue
            """
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    # sum is less than 0, move l ptr to the right
                    l += 1
                elif s > 0:
                    # sum is more than 0, move r ptr to the left
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
        return [list(i) for i in res]

if __name__ == "__main__":
    sum = Sum()
    nums = [-1,0,1,2,-1,-4]
    print(sum.three_sum(nums))
