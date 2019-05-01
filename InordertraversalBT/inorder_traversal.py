#!/usr/bin/python

def inorderTraversal(self, root):
    lst = []
    if root:
        if root.left:
            lst.extend(self.inorderTraversal(root.left))
        lst.append(root.val)
        if root.right:
            lst.extend(self.inorderTraversal(root.right))
    return lst
