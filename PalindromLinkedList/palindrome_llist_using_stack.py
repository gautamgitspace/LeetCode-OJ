#!/usr/bin/env python

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        # fetch mid
        slow = fast = cur = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next

        # now that slow is at mid, Push
        # the second half into the stack
        stack = [slow.val]
        while slow.next:
            slow = slow.next
            stack.append(slow.val)

        # Pop and compare with list elements
        while stack:
            if stack.pop() != cur.val:
                return False
            cur = cur.next

        return True
