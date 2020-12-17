class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        lst = [0 for i in range(n)]
        lst[0], lst[1] = 1, 2
        for i in range(2, n):
            lst[i] = lst[i - 1] + lst[i - 2]
        return lst[len(lst) - 1]