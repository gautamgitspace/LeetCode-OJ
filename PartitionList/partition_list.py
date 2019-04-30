#!/usr/bin/python

"""
idea is to maintain two lists and then link them.
head1 ----> tail1: is the list for elements smaller than pivot x
head2 ----> tail2: is the list for elements larger than pivot x
we keep adding to tail1 and tail2 and then stitch the two Lists:
stitch: tail1.next to head2.next
and return head1.next and terminate tail2.next as None.
"""
class Solution(object):
    def partition(self, head, x):
        head1 = tail1 = ListNode(0)
        head2 = tail2 = ListNode(0)

        while head:
            if head.val < x:
                tail1.next = head
                tail1 = tail1.next
            else:
                tail2.next = head
                tail2 = tail2.next
            head = head.next
        tail2.next = None
        tail1.next = head2.next
        return head1.next
