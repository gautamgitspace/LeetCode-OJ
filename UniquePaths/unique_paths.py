class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        """
        observation: total steps can be m + n - 2
        """

        # edge case
        if m <= 0 or n <= 0:
            return 0
        # start == finish case
        if m == 1 or n == 1:
            return 1

        # build an empty matrix
        matrix = [[1 for j in range(n)]for i in range(m)]
        # print matrix

        for i in range(1,m):
            for j in range(1,n):
                # keep recording for each m[i][j]
                # we can go down, m[i-1][j] or up, m[i][j-1]
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        # print(matrix)
        return matrix[-1][-1]
    
