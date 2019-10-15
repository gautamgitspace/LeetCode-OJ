class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        shifts = 0
        sorted_heights = sorted(heights)
        for i in range (len(heights)):
            if heights[i] != sorted_heights[i]:
                shifts += 1
        return shifts
