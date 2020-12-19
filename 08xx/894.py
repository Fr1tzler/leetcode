# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def allPossibleFBT(self, N):
        def all_FBT(N):
            if trees[N]:
                return trees[N]
            elif N % 2 == 0:
                return None
            elif N == 1:
                trees[1] = [TreeNode(0)]
                return [TreeNode(0)]
            else:
                result = []
                for i in range(1, N - 1):
                    left = all_FBT(i)
                    right = all_FBT(N - i - 1)
                    if left == None or right == None:
                        continue
                    for left_node in left:
                        for right_node in right:
                            result.append(TreeNode(0, left_node, right_node))
                trees[N] = result
                return result
    
        trees = [None for i in range(N + 1)]
        return all_FBT(N)