class Solution(object):
    def findNumbers(self, nums):
        result = 0
        for i in map(str, nums):
            result += 1 - len(i) % 2
        return result