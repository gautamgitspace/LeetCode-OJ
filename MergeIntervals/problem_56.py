#!/usr/bin/python
"""
c_s - current start
c_e - current end
l_c_s - last condensed start
l_c_e - last condensed end

KEY - What if we sorted our list of meetings by start time?
Then any meetings that could be merged would always be adjacent!
So we could sort our meetings, then walk through the sorted list
and see if each meeting can be merged with the one after it.

Sorting takes O(nlgn) time in the worst case. If we can then do the
merging in one pass, that's another O(n) time, for O(nlgn) overall.
if input is sorted, we can avoid sorting and it takes O(n) for time
and O(n) for space

* l_c_s and l_c_e needs to be updated with each comparison
* merging candidate is when - c_e is less than l_c_e
* if merging, start time will be l_c_s and max of (c_e and l_c_e)
* if not merging, just append normally

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
