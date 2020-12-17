class Solution(object):
    def maxDepth(self, s):
        result = 0
        current = 0
        for i in s:
            if i == "(":
                current += 1
            elif i == ")":
                if current > result:
                    result = current
                current -= 1
        return result