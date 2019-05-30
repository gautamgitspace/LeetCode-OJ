public class Solution {
  public boolean isValidBST (TreeNode root) {
    return isValidBST (root, Long.MIN_VALUE, Long.MAX_VALUE);
  }

  public boolean isValidBST (TreeNode root, long minVal, long maxVal) {
    if (root == null) return true;
    // condition that makes it false
    if (root.val >= maxVal || root.val <= minVal) return false;
    /*
    *  at each level, there's a new minVal and maxVal
    * in case of left traversal, maxVal will be that of root (all small nodes to the left)
    * in case of right traversal, minVal will be that of root (all big nodes to the right)
    */
    return isValidBST(root.left, minVal, root.val) && isValidBST(root.right, root.val, maxVal);
  }
}
