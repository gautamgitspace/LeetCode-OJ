#!/usr/bin/python

class Prune:
    def remove_elem(self, nums, val):
        while val in nums:
            print "hey"
            nums.remove(val)

        return len(nums)

if __name__ == "__main__":
    prune = Prune()
    print prune.remove_elem([1,2,3,4,4,4,5], 4)
