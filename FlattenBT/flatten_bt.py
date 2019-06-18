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

PRE-ORDER: 1,2,3,4,5,6
REV. PRE-ORDER [R, L, ROOT]: 6,5,4,3,2,1

So we gotta put root in prev in each iteration and make this prev the
right of current root everytime. and make left current root as None.\

Iteration 1:
------------

    6
  /   \
None  None

Iteration 2:
------------

prev = root = 6
current root = 5

    5
  /   \
None   6

Next, 5 becomes prev. and so on ...
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
