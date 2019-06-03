#!/usr/bin/python

"""
KEY - is to find the root from pre-order(1st element) or post-order(last element)
      and then to find the index of the root in the inorder list. Once this is done
      the problem is broken into two parts: left slice inorder and right slice inorder.

      Take care that in postorder, the right slice needs to be constructed first.
      WHY? - you should have the value you wanna pop in the inorder slice before
      you decide to pop it
"""
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            # find index of the root in inorder list
            index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[index])
            root.left = self.buildTree(preorder, inorder[0:index])
            root.right = self.buildTree(preorder, inorder[index+1:])
            return root

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            # find index of the root in inorder list
            index = inorder.index(postorder.pop())
            root = TreeNode(inorder[index])
            root.right = self.buildTree(inorder[index+1:], postorder)
            root.left = self.buildTree(inorder[:index], postorder)
            return root
