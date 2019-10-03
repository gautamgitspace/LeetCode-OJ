#!/usr/bin/env python

def right_side_view(self, root):
    visible = []
    if not root:
        return visibe
    levels = [root]
    while levels:
        size = len(levels)
        for i in range(levels):
            curr = levels.pop()
            if (i == size - 1):
                visible.add(curr.val)
            if root.right:
                levels.add(root.right)
            if root.left:
                levels.add(root.left)
    return visible
