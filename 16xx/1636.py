class Solution(object):
    def frequencySort(self, nums):
        dct = dict()
        for i in set(nums):
            dct[i] = nums.count(i) * 1000 - i
        nums.sort(key = lambda x: dct[x])
        return nums