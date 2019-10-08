class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = list()
        self.push_all(root)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        THOUGHT PROCESS:
        - next smallest will be in the left branch, if it exists
          otherwise search the right branch and traverse the left
          nodes in the right branch. Need to store all vals as we
          keep going left. last value stored will be smallest.
          We might just store one value and have to go to right
          branch and check left nodes there (left < right)
        - when left branch is returned, root will be returned
          before going to right branch
        - how to keep track of what already has been returned. or
          in other words, how to go backwards and keep track of
          parent of returned(now this parent is the next to be
          returned) - Use a stack?

        NOTES:
        0. pop from stack
        1. if the popped node has a right, it will push that on
        2. yield the val of the node popped

        next and hasNext run in O(1) avg time

        """
        temp_node = self.stack.pop()
        self.push_all(temp_node.right)
        return temp_node.val

    def push_all(self, node):
        """
        traverses left -> left nodes
        this is used for left nodes of the right branch as well
        """
        while node is not None:
            self.stack.append(node)
            node = node.left

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        # if there's something in the stack, we can return
        # a yay, otherwise, a nay
        return self.stack
