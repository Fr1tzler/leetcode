class Solution(object):
    def numberOfSteps (self, num):
        result = 0
        while (num > 0):
            if num % 2 == 1:
                result += 1
                num -= 1
            else:
                num //= 2
                result += 1
        return result