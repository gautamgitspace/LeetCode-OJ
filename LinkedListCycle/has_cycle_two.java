/*
 * KEY - SLOW and FAST never meet if the list is straight
 * They meet, if the list has a cycle. i.e. if they meet,
 * we return true iff asked - does list has a cycle?
 * if asked to return the point of loop, we move back SLOW
 * to head and increment both slow and fast by 1 step, until
 * they meet again. At that time, we can return slow or fast.
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                break;
            }
        }

        if (fast == null || fast.next == null) {
            return null;
        }
        slow = head;
        while (slow != fast) {
            slow = slow.next;
            fast = fast.next;
        }
        return fast;
    }
}
