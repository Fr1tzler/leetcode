class Solution(object):
    def checkPossibility(self, nums):
        counter = 0
        for i in range(len(nums - 1)):
            if nums[i] > nums[i + 1]:
                counter += 1
        return counter <= 1