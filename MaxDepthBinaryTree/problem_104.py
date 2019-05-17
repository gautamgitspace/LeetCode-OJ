#!/usr/bin/python

class Solution:
    def max_depth_a(self, root):
        if not root:
            return 0
        return 1 + max(max_depth_a(root.left), max_depth_a(root.right))

    def max_depth_b(self, root):
        if not root:
            return 0
        left_depth = right_depth = 0
        if root.left: left_depth = max_depth_b(root.left)
        if root.right: right_depth = max_depth_b(root.right)
        return max(left_depth, right_depth) + 1
