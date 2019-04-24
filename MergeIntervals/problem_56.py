#!/usr/bin/python
"""
c_s - current start
c_e - current end
l_c_s - last condensed start
l_c_e - last condensed end
"""
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        sorted_intervals = sorted(intervals)
        #base comparator
        condensed_intervals = [sorted_intervals[0]]
        
        """
        start goingg through elements in sorted_intervals
        starting from the 1st element.
        """
        for c_s, c_e in sorted_intervals[1:]:
            l_c_s, l_c_e = condensed_intervals[-1]

            if c_s <= l_c_e:
                # condense case
                condensed_intervals[-1] = [l_c_s, max(c_e, l_c_e)]
            else:
                # just append the current starts and ends case
                condensed_intervals.append((c_s, c_e))
        return condensed_intervals
