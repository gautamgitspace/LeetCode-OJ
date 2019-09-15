#!/usr/bin/env python

"""
Sample run
-----------
Input:
          4
        /   \
       3     5
      /       \
     2         6
    /           \
   1             7
Output:
       4
    /    \
   2      6
 /  \    /  \
1    3  5    7


approach A:
-----------
is to traverse nodes in Inorder and one by one
insert into a self-balancing BST like AVL tree. Time
complexity of this solution is O(n Log n)

approach B:
-----------
- Traverse given BST in inorder and store result in an array.
This step takes O(n) time.
- Build a balanced BST from the above created sorted array
using the recursive approach. This also takes O(n) as we
traverse each element exactly once. Processing each element
takes O(1) time.

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def traverse_and_store(self, root):
        container = []
        if root:
            self.traverse_and_store(root.left)
            container.append(root.val)
            self.traverse_and_store(root.right)
        return container

    def build_balanced_bst(self, container):
        l, r = 0, len(container)-1
        while l < r:
            mid = l + (r-l)/2
            node = Node(container[mid])
            node.left = self.build_balanced_bst(container[:mid-1])
            node.right = self.build_balanced_bst(container[mid+1:])
        return node

    def correct_skewed(self, root):
        container = self.traverse_and_store(root)
        balanced_bst_root = self.build_balanced_bst(container)
        return balanced_bst_root
