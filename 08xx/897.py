# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def increasingBST(self, root):
        def traverse(root):
            if root == None:
                return []
            return traverse(root.left) + [root.val] + traverse(root.right)

        values = traverse(root)
        head = TreeNode(None)
        curr = head
        for i in values:
            curr.right = TreeNode(i)
            curr = curr.right
        return head.right