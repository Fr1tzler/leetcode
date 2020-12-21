class Solution(object):
    def sortByBits(self, arr):
        arr.sort(key=lambda num: bin(num).count('1') * 10000 + num)
        return arr