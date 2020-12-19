class Solution(object):
    def sortedSquares(self, nums):
        res = [i * i for i in nums]
        res.sort()
        return res