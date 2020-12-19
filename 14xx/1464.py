class Solution(object):
    def maxProduct(self, nums):
        positive_0 = 0
        positive_1 = 0
        for i in nums:
            if i > positive_0:
                positive_1 = positive_0
                positive_0 = i
            elif i > positive_1:
                positive_1 = i
        return (positive_0 - 1) * (positive_1 - 1)