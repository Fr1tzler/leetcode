class Solution(object):
    def rangeSumBST(self, root, low, high):
        if root == None:
            return 0
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        return self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high) + root.val
