class Solution(object):
    def removeLeafNodes(self, root, target):
        if root == None:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if root.left == None and root.right == None and root.val == target:
            return None
        return root
