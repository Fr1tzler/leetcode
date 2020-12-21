class Solution(object):
    def countDigitOne(self, n):
        res = 0
        power_of_10 = 1
        while power_of_10 <= n:
            div = power_of_10 * 10
            res += (n // div) * power_of_10 + min(max(n % div - power_of_10 + 1, 0), power_of_10)            
            power_of_10 = div
        return res
