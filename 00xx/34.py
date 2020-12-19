class Solution:
    def binsearch(self, nums, target, to_left):
        left = 0
        right = len(nums)
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > target or (to_left and target == nums[middle]):
                right = middle
            else:
                left = middle + 1
        return left

    def searchRange(self, nums, target):
        left_idx = self.binsearch(nums, target, True)
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]
        return [left_idx, self.binsearch(nums, target, False) - 1]
