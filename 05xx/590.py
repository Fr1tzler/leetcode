class Solution(object):
    def postorder(self, root):
        if root == None:
            return
        res = []
        for child in root.children:
            res += self.postorder(child)
        return res + [root.val]
