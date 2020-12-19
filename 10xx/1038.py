class Solution(object):
    def bstToGst(self, root):
        def traversal(root, value):
            if root == None:
                return value
            root.val += traversal(root.right, value)
            left = traversal(root.left, root.val)
            return left

        traversal(root, 0)
        return root
