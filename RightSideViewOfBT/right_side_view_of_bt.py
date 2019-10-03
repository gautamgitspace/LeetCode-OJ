#!/usr/bin/env python
"""
idea is to always store the last element at each level.
If both left and right levels are same, then also last
and if one of them is bigger than the other, then also
last will be visible when stand to the right of the tree
"""

def right_side_view(self, root):
    visible = []
    if not root:
        return visibe
    # first level
    levels = [root]
    while levels:
        # this will be the # of elements
        # in the level order list. To start
        # with, we have just 1 i.e. root
        size = len(levels)
        for i in range(levels):
            # for every element we pop and
            # and check if size - 1 is the
            # current, if yes, this the last
            # node in the top-bottom sequence
            # and we want to capture it
            curr = levels.pop()
            if (i == size - 1):
                visible.add(curr.val)
            # usual mundane stuff
            if root.right:
                levels.add(root.right)
            if root.left:
                levels.add(root.left)
    return visible
