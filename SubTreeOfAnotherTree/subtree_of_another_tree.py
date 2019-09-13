class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool

        Q: is s subtree of t?
        A: need to check the same tree logic. if they match at root of
        s and t, we good. Else check if left of s and t match or if
        right of s and t match. if they do return true
        """
        if not s:
            return False;
        return self.is_same_tree(s,t) or\
        self.isSubtree(s.left, t) or\
        self.isSubtree(s.right, t)

    def is_same_tree(self, s, t):
        if not s and not t:
            return True
        return s and t and s.val == t.val and\
        self.is_same_tree(s.left, t.left) and\
        self.is_same_tree(s.right, t.right)

        return False
