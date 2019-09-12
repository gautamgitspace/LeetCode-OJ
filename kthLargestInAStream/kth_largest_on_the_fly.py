#!/usr/bin/env python
"""
The idea is to heapify the list and keep its size = k
at all times such that nums[0] will always contain the
kth largest and nums[-1] will always contain the largest
This is achieved by cutting short the heap

While adding to heap, add only if:
- check if len(heap) < k, if yes do a heapush of the val
  This will only be done when elements in heap are lt k
- check if the val is a replace candidate? i.e. is it
  greater than nums[0], if yes do a heapreplace which
  will pop the smallest and return (we don't need this)
  and insert the val
"""
import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        # cut short the heap, keep k elements
        # at most at any given time
        while len(self.nums) > k:
            heapq.heappop(self.nums)


    def add(self, val):
        #print 'evaluating val: ' + str(val)
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            #print 'comparing val ' + str(val) + ' with ' + str(self.nums[0])
            #print 'replace candidate? YES'
            heapq.heapreplace(self.nums, val)
        #print self.nums
        return self.nums[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
