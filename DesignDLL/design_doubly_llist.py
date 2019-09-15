#!/usr/bin/env python

class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.next = next
        self.prev = prev

    def add_at_front(self, head, data):
        new_node = Node(data)
        new_node.next = self.head
        head.prev = new_node
        new_node = head
        return new_node

    def add_after_given_node(self, head, data, node):
        curr = head
        while curr is not None:
            curr = curr.next
            if curr.val == data:
                break
        new_node = Node(data)
        temp = curr.next
        curr.next = new_node
        new_node.prev = curr
        new_node.next = temp
        temp.prev = new_node

    def add_at_end(self, head, data):
        # if list is empty, this is the only element
        new_node = Node(data)
        # since we have to add to the last,
        # this will be done regardless of
        # empty list or a list with elements
        new_node.next = None

        if head is None:
            new_node = head
            new_node.prev = None, None

        # when list is not empty, gotta traverse
        curr = head
        while curr.next is not None:
            curr = curr.next
            last = curr
        # now we gotta add after last
        last.next = new_node
        new_node.prev = last
