class Solution(object):
    def preorder(self, root):
        if root == None:
            return
        res = []
        for child in root.children:
            res += self.preorder(child)
        return [root.val] + res
