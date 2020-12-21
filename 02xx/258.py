class Solution(object):
    def addDigits(self, num):
        def iterate(num):
            return sum(map(int, list(str(num))))
        while num >= 10:
            num = iterate(num)
        return num
