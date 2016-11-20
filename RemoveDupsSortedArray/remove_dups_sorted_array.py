#!/usr/bin/env python
#LeetCode OJ Problem #29 - remove duplicates and return length of resulting array
#KEY - We actually do not want to track dups and remove, we just want to return the Length
#of the array without dups.

def removeDuplicates(numbers):
    i = 0
    for j in range(1, len(numbers)):
        if numbers[j] != numbers[i]:
            i+=1
            numbers[i] = numbers[j]
    return i+1
numbers = [2,3,6,9,11,17,17,18,18,18,18]

print 'Length before dup removal:', len(numbers)
print 'Length after dup removal:', removeDuplicates(numbers)
