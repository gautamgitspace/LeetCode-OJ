#!/usr/bin/python

def containsDuplicate(self, nums):
    if not nums:
        return False
    unique = []
    for items in nums:
        if items not in unique:
            unique.append(items)
        else:
            return True
    return False
    
def one_liner(self, nums):
    return len(set(nums)) != len(nums)
