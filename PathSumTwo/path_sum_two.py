#!/usr/bin/python

class Solution(object):
    def hasPathSum(self, root, sum):
        if not root:
            return []
        res = []
        self.dfs(root, sum, [], res)

        def dfs(self, root, sum, stitch, res):
            if root.val == sum and not root.left and not root.right:
                stitch.append(root.val)
                res.append(stitch)
            if root.left:
                self.dfs(root.left, sum - root.val, stich + [root.val], res)
            if root.right:
                self.dfs(root.right, sum - root.val, stich + [root.val], res)
