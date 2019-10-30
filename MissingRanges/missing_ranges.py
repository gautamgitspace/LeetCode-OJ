#!/usr/bin/env python

import itertools

def missing_ranges(nums, l, u):
    res = []
    # make last_num one less than lower
    last_num = l - 1

    # adjust nums by including upper in nums
    for num in itertools.chain(nums, [u + 1]):
        # we mad last_num one less than lower
        # now check one more than lower with
        # num (iterator of nums)
        if last_num + 2 == num:
            # take example of [5,6,,,20] and l = 4
            # we go one behind l, so last_num = 3
            # now we go 2 ahead of last_num so it
            # becomes 5 which is nums[0]. so what is
            # missing? just l itself. so add
            # last_num to res
            res.append(str(last_num + 1))
        elif last_num + 2 < num:
            # take example of [5,6,,,,20] and l = 2
            # last_num becomes 1, we go 2 ahead it
            # becomes 3. now 3 < 5. what is missing?
            # 2->4 which is nothing but last_num + 1
            # and num - 1
            res.append( '{}->{}'.format(last_num + 1, num - 1))

        last_num = num

    return res

if __name__ == "__main__":
    nums = [5, 6, 8, 12, 15]
    print nums
    print missing_ranges(nums, 4, 20)
