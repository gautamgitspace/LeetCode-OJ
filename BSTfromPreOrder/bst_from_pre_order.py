#!/usr/bin/python
'''
Gen BST from given list of preorder

KEY is to start with having root in place which is the
first element of preorder. after that we have to find
the pivot index (root), towards the left of which all
elements are smaller and towards the right of which all
elements are bigger.

i.e if (preorder[i] > root.val)
'''
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        node = TreeNode(preorder[0])
        i = 0
        for i in range(len(preorder)):
            if preorder[i] > node.val:
                break
            i += 1

        node.left = self.bstFromPreorder(preorder[1:i])
        node.right = self.bstFromPreorder(preorder[i:])
        return node

    def anotherOne(self, preorder):
        if not preorder:
            return None
        node = TreeNode(preorder[0])

        # fabrcate new left and right pruned preorder lists
        left = [v for v in preorder[1:] if v < node.val]
        right = [v for v in preorder[len(left)+1:] if v > node.val]

        node.left = self.bstFromPreorder(left)
        node.right = self.bstFromPreorder(right)

        return node
