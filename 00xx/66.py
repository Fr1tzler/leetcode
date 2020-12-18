class Solution(object):
    def plusOne(self, digits):
        digits[-1] += 1
        i = len(digits) - 1
        while digits[i] >= 10 and i != 0:
            digits[i] -= 10
            digits[i - 1] += 1
            i -= 1
        if i == 0 and digits[i] >= 10:
            digits[i] -= 10
            digits.insert(0, 1)
        return digits
    def __init__(self):
        pass