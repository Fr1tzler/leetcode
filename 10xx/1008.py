class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        def insert_node(node, root):
            if node > root.val:
                if root.right != None:
                    insert_node(node, root.right)
                else:
                    root.right = TreeNode(node)
            else:
                if root.left != None:
                    insert_node(node, root.left)
                else:
                    root.left = TreeNode(node)
        
        root = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            insert_node(preorder[i], root)
        return root