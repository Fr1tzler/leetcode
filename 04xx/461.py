class Solution(object):
    def hammingDistance(self, x, y):
        z = x ^ y
        res = 0
        while z:
            res += z % 2
            z //= 2
        return res