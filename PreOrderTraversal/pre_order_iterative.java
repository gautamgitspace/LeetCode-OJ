/*
 * PRE-ORDER TRAVERSAL, ITERATIVE
 * res, a list to contain all the visiting nodes
 * visiting, a TreeNode to contain current visiting node
 * toVisit, a stack to conatin right and left of visiting
 * pop from toVisit and put in visiting one by one
 **/

public List<Integer> preOrder (TreeNode root) {
  List<Integer> res = new LinkedList<Integer>();
  if (root == null) return res;
  Stack<TreeNode> toVisit = new Stack<TreeNode>();
  toVisit.push(root);
  while(!toVisit.empty()) {
    TreeNode visiting = toVisit.pop();
    res.add(visiting.val);
    if (visiting.left != null) toVisit.push(visiting.left);
    if (visiting.right != null) toVisit.push(visting.right);
  }
  return res;
}
