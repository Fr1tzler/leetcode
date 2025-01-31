# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def insertIntoBST(self, root, val):
        if root == None:
            return TreeNode(val)
        if root.val > val:
            if root.left == None:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left, val)
        else:
            if root.right == None:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right, val)
        return root