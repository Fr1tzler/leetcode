class Solution(object):
    def divide(self, dividend, divisor):
        sign = 1
        if dividend < 0:
            sign *= -1
            dividend *= -1
        if divisor < 0:
            sign *= -1
            divisor *= -1
        result = sign * (dividend // divisor)
        if result > 2 ** 31 - 1:
            result = 2 ** 31 - 1
        return result