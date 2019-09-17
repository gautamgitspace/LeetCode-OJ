class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode

        THOUGHT PROCESS:
        - if key is less than root, need to delete in left sub,
          otherwise in right sub
        - else it is the root to be deleted now this can have just
          left sub or just right sub or both. Cases for all below
        - just left sub: delelte the node, new root will be root.left
        - just right sub: delete the node, new root will be root.right
        - both right and left. Hmmm.. tricky
          We replace the root with the minimum value in the RIGHT SUB
          and delete that node in the RIGHT SUB. Note that this minimum
          value can be somewhere in the left branches in the RIGHT SUB
        """
        if not root:return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            # root delete case: just left sub, just right sub,
            # both right and left sub
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            # else tricky case
            temp = root.right
            while temp.left:
                # keep going left iff left exists
                # minimum of RIGHT SUB will lie in
                # the LEFT BRANCHES
                temp = temp.left
            root.val = temp.val
            root.right = self.deleteNode(root.right, root.val)
        return root
