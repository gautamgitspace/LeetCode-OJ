#!/usr/bin/python
"""
0. DFS recursive approach.
1. TODO BFS (using queue)
2. TODO DFS (using stack)
"""

class Solution(object):
    def binaryTreePaths(self, root):
        if not root:
            return []
        paths = []
        self.dfs (root, "", paths)
        return paths

    def dfs(self, root, stitch, paths):
        if not root.left and not root.right:
            paths.append(stitch + str(root.val))
        if root.left:
            self.dfs(root.left, stitch + str(root.val) + "->", paths)
        if root.right:
            self.dfs(root.right, stitch + str(root.val) + "->", paths)
