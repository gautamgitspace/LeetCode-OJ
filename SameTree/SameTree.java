public boolean isSameTree(TreeNode p, TreeNode q)
{
    if(p == null && q == null)
        return true;
    if(p == null || q == null)
        return false;
    boolean isLeftSame = isSameTree(p.left, q.left);
    boolean isRightSame = isSameTree(p.right, q.right);

    return p.data == q.data && isLeftSame && isRightSame;
}
