class Solution(object):
    def searchBST(self, root, val):
        if root == None:
            return None
        if root.val > val:
            return self.searchBST(root.left, val)
        elif root.val < val:
            return self.searchBST(root.right, val)
        return root