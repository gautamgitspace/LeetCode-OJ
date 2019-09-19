class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        """
        clockwise is dist from S to D
        anti-clockwise will always be: 0th node -> S + D -> 0th node
        i.e. in slicing language, it will be [:start] + [destination:]
        """
        start, destination =  sorted([start, destination])
        return distance[0] if len(distance) == 1 else\
        min(sum(distance[start:destination]), sum(distance[:start])\
        + sum(distance[destination:]))
            
