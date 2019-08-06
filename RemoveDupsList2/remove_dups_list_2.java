/*
Given a sorted linked list, delete all nodes that have
duplicate numbers, leaving only distinct numbers from the
original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5


KEY is to maintain two ptrs. PRE(vious) and CUR(rent). Any node that is unique will
fullfil the condition: pre.val != cur.val && cur.val != cur.next.val. If such a node
is found, append it to the resultant list, and update the resultant list pointer.

To start with, we don't have a pre so we take a dummy node and mark its next to head.

Else, update the pre to becmoe cur and cur to become next of cur.

Special case - last node needs to be dealt separately
*/

class Solution {
  public ListNode deleteDuplicatesFromSortedList(ListNode head)
  if (head == null) return null;
    ListNode dummy = new ListNode( head.val == 0 ? 1 : 0);

    dummy.next = head;
    ListNode pre = dummy;
    ListNode cur = head;
    ListNode first = dummy;

    while (cur != null && cur.next != null) {
      if (pre.val != cur.val && cur.val != cur.next.val) {
        /* we have a unique node at cur, add it
         * to the tail of first and update first
         */
        first.next = cur;
        first = first.next;
      }
      /* move-on, update pre and cur */
      pre = cur
      cur = cur.next;
    }
    /* deal with the last node */
    if (pre.val != cur.val) {
      first.next = cur;
      first = first.next;
    }
    /* tear the list now, rest of it has dups */
    first.next = null;
    return dummy.next;
  }
}
