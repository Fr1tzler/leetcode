class Solution(object):
    def minSubsequence(self, nums):
        nums.sort(reverse=True)
        s = sum(nums)
        res = []
        half_s = 0
        for i in nums:
            half_s += i
            res.append(i)
            if 2 * half_s > s:
                return res