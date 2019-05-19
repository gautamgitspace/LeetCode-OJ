class Solution {
    public int minDepth(TreeNode root) {
        if (root == null) return 0;
        int left_depth = minDepth(root.left);
        int right_depth = minDepth(root.right);
        return (left_depth == 0 || right_depth ==0) ? left_depth + right_depth + 1 : Math.min(left_depth, right_depth) + 1;
    }
}
