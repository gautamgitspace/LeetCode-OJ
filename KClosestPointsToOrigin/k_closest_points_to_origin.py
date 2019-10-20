import math
import heapq

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        dist, res = [], []
        for item in points:
            x, y = item
            proximity = math.sqrt(math.pow((x - 0),2) + math.pow((y - 0),2))
            heapq.heappush(dist, (proximity, x, y))
        while K:
            cherry = heapq.heappop(dist)[1:3]
            res.append(list(cherry))
            K -= 1
        return res
