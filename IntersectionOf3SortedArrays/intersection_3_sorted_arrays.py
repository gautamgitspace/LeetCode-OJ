#!/usr/bin/env python
from collections import Counter

"""
one liners for intersection and union
"""
def intersection(arr1, arr2, arr3):
    return list((Counter(arr1) & Counter(arr2) & Counter(arr3)).elements())

def union(arr1, arr2, arr3):
    return set((Counter(arr1) + Counter(arr2) + Counter(arr3)).elements())


"""
solutions using pointers
"""

def intersection_ptrs(arr1, arr2, arr3):
    i, j, k = 0, 0, 0
    res = []
    len1, len2, len3 = len(arr1), len(arr2), len(arr3)
    while i < len1 and j < len2 and k < len3:
        if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
            res.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1
    return res


def union_ptrs(arr1, arr2):
    """
    union using 3 ptrs, doesn't take
    into account arrays with duplicates
    """
    len1, len2 = len(arr1), len(arr2)
    i, j = 0, 0
    res = []
    while i < len1 and j < len2:
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            res.append(arr2[j])
            j += 1
        else:
            # can append either i or j
            res.append(arr1[j])
            i += 1
            j += 1
    while i < len1:
        res.append(arr1[i])
        i += 1
    while j < len2:
        res.append(arr2[j])
        j += 1
    return res

if __name__ == "__main__":
    arr1 = [1,2,3,14,5]
    arr2 = [1,12,14,17,19]
    arr3 = [1,3,14,5,8]
    print intersection_ptrs(arr1, arr2, arr3)
    print union_ptrs(arr1, arr2)
