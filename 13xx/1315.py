class Solution(object):
    def sumEvenGrandparent(self, root):
        def DFS(root, father_even, grandpa_even):
            if root == None:
                return 0
            result = 0
            if grandpa_even:
                result += root.val
            currrent_even = root.val % 2 == 0
            result += DFS(root.left, currrent_even, father_even)
            result += DFS(root.right, currrent_even, father_even)
            return result
        
        return DFS(root, False, False)
