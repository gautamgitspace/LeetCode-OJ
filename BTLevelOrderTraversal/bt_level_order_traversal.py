#!/usr/bin/python
"""
KEY - track current nodes, next level nodes in separate lists
      keep appending current to result, keep updating level to
      next_level
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        level = [root]

        while root and level:
            current_nodes = []
            next_level = []
            for node in level:
                current_nodes.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            result.append(current_nodes)
            level = next_level

        return result

    def levelOrderReverse(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        level = [root]

        while root and level:
            current_nodes = []
            next_level = []
            for node in level:
                current_nodes.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            result.append(current_nodes)
            level = next_level

        return result[::-1]
