class Solution(object):
    def reverse(self, x):
        s = 1
        if x != 0:
            s = x // abs(x)
        x = abs(x)
        while(x % 10 == 0 and x > 0):
            x //= 10
        lst = list(str(x))
        lst.reverse()
        res = int(''.join(lst)) * s
        if res >= 2**31 - 1 or res <= -2**31:
            res = 0
        return res