class Solution {
    public ListNode reverseList(ListNode head) {
        return reverseListRecursive(head, null);
    }
    // we operate on head i.e. 1 and newHead i.e null to begin with
    ListNode reverseListRecursive(ListNode head, ListNode newHead) {
        if (head == null)
            return newHead;
        // store next i.e. 2
        ListNode next = head.next;
        // make next of 1 null
        head.next = newHead;
        /* we pass the node to operate on i.e. next
         * and the next guy to link it to, i.e. head
         * which is nothing but 1 in this case and
         * will become 2 in the next iteration
         */
        return reverseListRecursive(next, head);
    }
}
