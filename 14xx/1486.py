class Solution(object):
    def xorOperation(self, n, start):
        result = start
        current = start
        for i in range(1, n):
            current += 2
            result = result ^ current
        return result
