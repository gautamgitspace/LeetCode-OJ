class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root and root.val < val:
            root = self.searchBST(root.right, val)
        if root and root.val > val:
            root = self.searchBST(root.left, val)
        if root and root.val == val:
            return root
