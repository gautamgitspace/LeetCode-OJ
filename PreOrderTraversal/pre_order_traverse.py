#!/usr/bin/python
"""
RECURSIVE APPROACH
"""
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lst = []
        if root:
            lst.append(root.val)
            if root.left:
                lst.extend(self.preorderTraversal(root.left))
            if root.right:
                lst.extend(self.preorderTraversal(root.right))
        return lst
