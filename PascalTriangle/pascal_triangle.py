class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        """
        in [ [1], [1,1], [1,1,1] ]:
        we need to add the first and the second indices
        of the last generated row.

        which means we gotta do: p[-1][0] + p[-1][1]
        where -1 is the very last row and 0 is the first
        index and 1 is the last index.

        Now extend this logic to all layers
        """
        # manufacture pascal base
        pascal = [[1]*(i+1) for i in range(numRows)]
        # do the calculation
        for i in range(numRows):
            for j in range(1, i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal
