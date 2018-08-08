bool isMirror(struct TreeNode*, struct TreeNode*);

bool isMirror(struct TreeNode* root1, struct TreeNode* root2) {
    /* empty tree case */
    if (root1 == NULL && root2 == NULL) {
        return true;
    }
    
    if (root1 && root2 && root1->val == root2->val) {
        return isMirror(root1->left, root2->right) &&
               isMirror(root1->right, root2->left);
    }
    
    return false;
}

bool isSymmetric(struct TreeNode* root) {
    return isMirror (root, root);
}
