class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """
        THOUGHT PROCESS:
        this can be solved by running sum approach

        say for array [3,2,5,3,2,4] and k = 10,
        running sum:  [3,5,10,13,15,19]

        now in the running sum array we notice that
        there are three stretches where k can be 10.

        These are: 3 -> 13, 5 -> 15 and also 0 -> 10
        the last case is special and comes when we have k
        in the running sum itself

        now we need to build a dict such that key is running
        sum element and value is the number of times that
        running sum element appears in the running sum array

        we start with d[0] = 1 for the special case of 0->10

        we keep on calculating running sum index by index and
        check if [running element - k] is present in the dict.
        If it is, we add 1 (or the val at that key per say) to
        count.

        Note that from previous discussion:
        we have established that [running element - k]
        is a stretch where k is 10
        """
        count = 0
        sums = 0
        d = dict()
        d[0] = 1

        for i in range(len(nums)):
            sums += nums[i]             # running sum element calc
            count += d.get(sums-k,0)    # check if [running element - k] exists in d
            d[sums] = d.get(sums,0) + 1 # add running sum element to d
            # print d
        return(count)
