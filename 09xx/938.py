# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rangeSumBST(self, root, low, high):
        if root.val > high:
            return
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        