#!/usr/bin/env python3
"""
in order to find out the maximum distance between any two arrays,
we need not compare every element of the arrays, since the arrays
are already sorted. Thus, we can consider only the extreme points
in the arrays to do the distance calculations.

We also want to take care that max dist is not between the elements
of the same array. Thus, for arrays aa and bb currently chosen, we can
just find the maximum out of a[n-1]-b[0]a[n−1]−b[0] and
b[m-1]-a[0]b[m−1]−a[0] to find the larger distance

we can begin our comparison and distance calculation process by having
minimum and maximum values from the first array start and end
"""
def max_dist(arrays):
    res, minimum, maximum = 0, arrays[0][0], arrays[0][-1]
    for i in range (1, len(arrays)):
        res = max(res, max(maximum - arrays[i][0], arrays[i][-1]) - minimum)
        minimum = min(minimum, arrays[i][0])
        maximum = max(maximum, arrays[i][-1])
    return res

if __name__ == "__main__":
    arrays = [[1,2,3], [4,5], [1,2,3]]
    print (max_dist(arrays))
