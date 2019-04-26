#!/usr/bin/python

class Solution:
    def plus_one(self, nums):
        token = ""
        res_list = []
        for items in nums:
            token += str(items)
        result = str(int(token)+1)

        for alphabets in result:
            res_list.append(alphabets)
        return res_list

if __name__ == '__main__':
    sol = Solution()
    print sol.plus_one([4,3,2,9])
