class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        """
        not visited = 0
        being visite = -1
        visited, done = 1

        if while doing dfs, we see visited[i] == -1 => LOOP
        if while doing dfs, we see visited[i] ==  1 => NO LOOP

        for case [[0,1], [1,2], [2,3]]
        we will have graph as [[1], [2], [3], []]
        what this means is:
        0th(index) node points to 1, 1st(index) node points to 2
        2nd(index) node points to 3, 3rd(index) nodes points to none


        for case [[0,1], [1,2], [2,3], [3,0]]
        we will have graph as [[1], [2], [3], []]
        what this means is:
        0th(index) node points to 1, 1st(index) node points to 2
        2nd(index) node points to 3, 3rd(index) nodes points back to 0
        """
        graph = [[] for _ in xrange(numCourses)]
        visited = [0 for _ in xrange(numCourses)]

        # create graph
        for x, y in prerequisites:
            graph[x].append(y)
            #print graph

        # visit nodes using dfs
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True

    def dfs(self, graph, visited, i):
        # node is already visited, we have a loop
        #print visited
        if visited[i] == -1:
            return False
        # node is done being visited, we don't have a loop
        if visited[i] == 1:
            return True
        # being visited
        visited[i] = -1
        # visit all neighbors
        for j in graph[i]:
            #print i
            if not self.dfs(graph, visited, j):
                return False
        # after we have visited all the neihbors through
        # above DFS loop, we mark them as visited and done
        visited[i] = 1
        return True
