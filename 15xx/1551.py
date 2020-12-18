class Solution(object):
    def minOperations(self, n):
        a = n // 2
        if n % 2 == 1:
            return a * (a + 1) 
        return a * a