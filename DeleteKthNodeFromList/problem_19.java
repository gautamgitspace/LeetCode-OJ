class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
         if (head == null) {
            return null;
        }

        ListNode removeNode = findNthFromEnd(head, n);
         if (head == removeNode) {
           // we have to delete the very first node
           head = head.next;
           return head;
        }
        ListNode prev = head;
        ListNode iterator = head;
        while(iterator.next != removeNode.next) {
            prev = iterator;
            iterator = iterator.next;
            }
        prev.next = removeNode.next;
        return head;
        }


    public ListNode findNthFromEnd(ListNode head, int n) {
        ListNode ptr1 = head;
        ListNode ptr2 = head;
        for (int i = 0; i < n; i++) {
            // Move ptr2 n steps forward
            ptr2 = ptr2.next;
        }
        while (ptr2 != null) {
            /* Move ptr1 from start and ptr2 from
             * it's previous position one step at
             * a time until ptr2 reaches the end
             * of list */
            ptr1 = ptr1.next;
            ptr2 = ptr2.next;
        }
        return ptr1;
    }
}
