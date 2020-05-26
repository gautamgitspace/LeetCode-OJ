#!/usr/bin/env python

"""
In this problem where we have to return the maximum
length of the subarray that sums up to k.

Here we store d[running sum] : index and we start with
0 : -1 meaning that running sum of 0 is at index -1 (before 0)

Then if running sum - k is found in dict,  we store the length
of sub array in max. length will be given by current index -
index stored in dict.

Note that running sum elem1 - running sum elem2 = k. Hence,
existence of (running sum - k) is what we are looking for in
the hash table

if not found, we store the sum in d against its index or update
it if it already exists
"""
def max_sub_array_sum_equal_k(nums, k):
    sums = {}
    sums[0] = -1
    cur_sum, max_len = 0, 0
    for i in range(len(nums)):
        cur_sum += nums[i]
        # if cur_sum == k:
        #     max_len = i + 1
        if cur_sum - k in sums:
            max_len = max(max_len, i - sums[cur_sum - k])
        if cur_sum not in sums:
            sums[cur_sum] = i  # Only keep the smallest index.
    return max_len


if __name__ == "__main__":
    nums = [1, -1, 5, -2, 3]
    k = 3
    print max_sub_array_sum_equal_k(nums, k)
