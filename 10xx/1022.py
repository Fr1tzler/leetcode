class Solution:
    def sumRootToLeaf(self, root):
        result = [0]

        def DFS(root, curr_number, result):
            if root:
                curr_number = curr_number * 2 | root.val
                if not (root.left or root.right):
                    result[0] += curr_number
                DFS(root.left, curr_number, result)
                DFS(root.right, curr_number, result) 
        
        DFS(root, 0, result)
        return result[0]
