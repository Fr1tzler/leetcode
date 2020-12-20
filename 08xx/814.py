class Solution(object):
    def pruneTree(self, root):
        def contains_one(root):
            if root == None:
                return False
            if not contains_one(root.left):
                root.left = None
            if not contains_one(root.right):
                root.right = None
            return root.val == 1 or contains_one(root.left) or contains_one(root.right)
        
        if contains_one(root):
            return root
        return None
        