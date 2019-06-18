/* KEY is to check the height of each subtree as we recurse down the root.
 * On each node, we keep on getting heights of L and R subtrees. If subtree
 * is balanced, checkHeight will return actual height i.e. 1 + max of left
 * and right, if not balanced, it will return -1. In main, we stop whenever
 * the return value is -1 and we break out and return false.
 */
class Solution {
    public boolean isBalanced(TreeNode root) {
        if(checkHeight(root) == -1) return false;
        else return true;
    }

    static int checkHeight(TreeNode root)
    {
        if(root == null) return 0;

        int leftHeight = checkHeight(root.left);
        int rightHeight = checkHeight(root.right);

        if(leftHeight == -1 || rightHeight == -1) return -1;

        int diffInHeight = leftHeight - rightHeight;

        if(Math.abs(diffInHeight) > 1) {
            return -1;
        } else {
            return 1 + Math.max(leftHeight,rightHeight);
        }
    }
}
