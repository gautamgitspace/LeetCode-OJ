#!/usr/bin/python

"""
Given input:

    1
   / \
  2   5
 / \   \
3   4   6

The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
This needs to be done in place

KEY - is that flatten tree looks like the pre-order of the given BT.

Also, if we look closely, flatten tree looks like the reverse order of
a pre-order. i.e. PRE-ORDER = [ROOT, L, R] and reverse order of pre-order
= [R, L, ROOT]

So we gotta put root in prev in each iteration and make this prev the
right of current root everytime. and make left current root as None.
"""

class Solution (object):
    def __init__(self):
        self.prev = None
    def flatten(self, root):
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root
