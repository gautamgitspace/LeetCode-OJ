/*
 * KEY - Keep updating the sum fed to the next level
 * i.e. Deduct value of current root (at each level)
 * from total sum.
 */
class Solution {
public:
    bool hasPathSum(TreeNode* root, int sum) {
        if (root == NULL) return false;
        if ((root->val == sum) && (root->left == NULL) && (root->right == NULL)) return true;
        return hasPathSum(root->left, sum - root->val) || hasPathSum(root->right, sum - root->val);
    }
};
