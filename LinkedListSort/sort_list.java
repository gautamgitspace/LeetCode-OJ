"""
sort a linked list in O(nlogn)
- recursively find middle and fabricate left and right
- recursively merge sort left and right (if left is smaller, start with left otherwise with right)
"""

class Solution {
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null)
            return head;

        ListNode middle = getMiddle(head);
        ListNode nextOfMiddle = middle.next;
        middle.next = null;

        ListNode left = sortList(head);
        ListNode right = sortList(nextOfMiddle);

        ListNode sortedHead = sortedMerge(left, right);

        return sortedHead;
    }

    public ListNode sortedMerge(ListNode a, ListNode b) {
        ListNode result = null;

        if (a == null)
            return b;
        if (b == null)
            return a;
        if (a.val < b.val) {
            result = a;
            result.next = sortedMerge(a.next, b);
        } else {
            result = b;
            result.next = sortedMerge(a, b.next);
        }
        return result;
    }

    public ListNode getMiddle(ListNode head) {
        ListNode fast = head.next;
        ListNode slow = head;

        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        return slow;
    }
}
