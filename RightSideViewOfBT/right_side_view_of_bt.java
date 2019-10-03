class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> visible = new ArrayList<>();
        if (root == null)
            return visible;
        Queue<TreeNode> levels = new LinkedList<>();
        levels.add(root);
        while (!levels.isEmpty()) {
            int size = levels.size();
            for (int i=0; i<size; i++) {
                TreeNode curr = levels.remove();
                if (i == (size - 1))
                    visible.add(curr.val);
            if (curr.left != null)
                levels.add(curr.left);
            if (curr.right != null)
                levels.add(curr.right);
            }
        }
        return visible;
    }
}
