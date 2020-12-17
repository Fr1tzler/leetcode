class Solution(object):
    def sumZero(self, n):
        result = []
        sum = 0
        if n == 1:
            return [0]
        for i in range(1, n):
            result.append(i)
            sum += i
        result.append(-sum)
        return result