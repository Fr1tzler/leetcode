class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        def construct_tree(nums):
            if len(nums) == 0:
                return None
            max_elem = max(nums)
            position = nums.index(max_elem)
            return TreeNode(max_elem,construct_tree(nums[ : position]), construct_tree(nums[position + 1 : ]))        
        
        return construct_tree(nums)