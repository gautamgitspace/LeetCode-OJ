/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

bool isBST(struct TreeNode*, int, int);

bool isBST(struct TreeNode* root, int min, int max) {
    if (root == NULL)
        return true;
    if (root && root->left)
        if (root->val == INT_MIN && (root->left->val == INT_MIN) || (root->left->val == INT_MAX))
            return false;
    if (root && root->right)
        if (root->val == INT_MAX && (root->right->val == INT_MAX) || (root->right->val == INT_MIN))
            return false;
    if (root->val <= max && root->val >= min) {
        return isBST(root->left, min, root->val-1) && isBST(root->right, root->val+1, max);
    }
    else
        return false;
}

bool isValidBST(struct TreeNode* root) {
    return isBST(root, INT_MIN, INT_MAX);
}
