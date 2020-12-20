class Solution(object):
    def heightChecker(self, heights):
        target = sorted(heights)
        res = 0
        for i in range(len(heights)):
            if heights[i] != target[i]:
                res += 1
        return res