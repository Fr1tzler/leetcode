class Solution(object):
    def maxDepth(self, root):
        def depth(root):
            if root == None:
                return 0
            max_child_depth = 0
            for child in root.children:
                max_child_depth = max(max_child_depth, depth(child))
            return max_child_depth + 1

        return depth(root)