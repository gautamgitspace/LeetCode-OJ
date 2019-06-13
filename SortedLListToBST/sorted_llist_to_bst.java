/*
* KEY - Find mid using slow and fast runner. Build left and right sub-trees using the new mid 
*/

class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        if (head == null) return null;
        return genBSTHelper(head, null);
    }

    public TreeNode genBSTHelper(ListNode head, ListNode tail) {
        /* slow-runner, fast-runner approach to find mid */
        ListNode slow = head;
        ListNode fast = head;

        /* exit condition */
        if (head == tail) return null;

        while (fast != tail && fast.next != tail) {
            fast = fast.next.next;
            slow = slow.next;
        }
        /* at this point slow has reached mid */
        TreeNode root = new TreeNode(slow.val);
        root.left = genBSTHelper(head, slow);
        root.right = genBSTHelper(slow.next, tail);

        return root;
    }
}
