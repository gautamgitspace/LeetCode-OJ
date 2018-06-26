class TreeNode:
    self.val = None
    self.right = None
    self.left = None

    def __init__(self, val):
        self.val = val

def defectiveNode(TreeNode root):
    parents = [root]
    children = []
    defective = []

    while len(parent)!=None:
        for parent in parents:
            if parent.left!=None:
                if parent.left in children:
                    #add to defective and de-link the node
                    defective.append(parent.left)
                    parent.left = None
                else:
                    children.append(parent.left)
            if parent.right!=None:
                if parent.right in children:
                    defective.append(parent.right)
                    parent.right = None
                else:
                    children.append(parent.right)

        #update parent to be children at next level
        parent = children
        #update children to be new borns at next level
        children = []
        
    return defective
