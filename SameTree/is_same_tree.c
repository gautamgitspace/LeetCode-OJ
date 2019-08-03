bool isSameTree(struct TreeNode* p, struct TreeNode* q) {
    if ( p == NULL && q == NULL )
        return true;
    if ( p !=NULL && q !=NULL ) {
        if ( p->val == q->val && isSameTree(p->left, q->left) && isSameTree(p->right,q->right))
        return true;
    }
    return false;
}
