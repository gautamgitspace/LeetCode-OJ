#!/usr/bin/python

"""
[1,1,2,2,3,3,3,4]  becomes [1,1,2,2,3,3,4] and returns lengh 7

* key -> sorted, so numbers won't appear our of order
* clause -> CANNOT allocate memory to new lists/arrays
* how -> keep scanning subsequent occurring indices and if exceeds count of 2, i.e. seen for the 3rd time, move it to the last or just delete it (this maintains the len of list)
"""

def _prune (arr):
    count = 1
    length = len(arr)
    i = 1
    while i < length:
        if arr[i] == arr[i-1]:
            print str(arr[i]) + " matches " + str(arr[i-1])
            count += 1
        else:
            count = 1
        if count > 2:
            del arr[i]
            length -= 1
        else:
            i += 1
    return len(arr), arr

arr = [1,1,1,2,2,3,3,4,4,4,4]
print _prune(arr)
