/*
 * Q: Reverse a list in place
 * KEY is to use 3 pointers and keep swapping as we go
 * 1 > 2 > 3 > 4 > 5 > null
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode curr = head;
        ListNode prev = null;
        ListNode next = null;

        while (curr != null) {
            // save next i.e. 2
            next = curr.next;
            // link 1 to null
            curr.next = prev;
            // make 1 prev
            prev = curr;
            // make 2 curr
            curr = next;
        }
        return prev;
    }
}
