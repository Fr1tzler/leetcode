class Solution(object):
    def minAddToMakeValid(self, S):
        delta = 0
        res = 0
        for i in S:
            if i == '(':
                delta += 1
            else:
                delta -= 1
            if delta == -1:
                delta += 1
                res += 1
        return res + delta