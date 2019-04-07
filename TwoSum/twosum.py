#!/usr/bin/env python
# LEETCODE OJ PROBLEM 1: Given an array of integers, return indices of the two numbers such that they add up to a specific target.
def two_sum_all_numbers(array, target):
    distinguisher = set()
    result = []
    for item in array:
        diff = target-item
        if item not in distinguisher:
            distinguisher.add(diff)
        else:
            result.append(item)
            result.append(diff)
    return result
def two_sum_indices(array, target):
    distinguisher = set()
    result = []
    for i, item in enumerate (array):
        diff = target-item
        if item not in distinguisher:
            distinguisher.add(diff)
        else:
            result.append(i)
            result.append(array.index(diff))
    return sorted(result)

print "NUMBERS THAT MAKE THE TARGET:", two_sum_all_numbers(array=[3,0,6], target=6)
#print "INDICES OF NUMBERS THAT MAKE THE TARGET:", two_sum_indices(array=[-1,2,7], target=6)
