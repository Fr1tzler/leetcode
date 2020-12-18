class Solution(object):
    def checkPossibility(self, nums):
        def ascending(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return False
            return True
        
        left, right = 0, len(nums) - 1
        while left + 2 < len(nums) and nums[left] <= nums[left + 1] <= nums[left + 2]:
            left += 1
        while right - 2 >= 0 and nums[right - 2] <= nums[right - 1] <= nums[right]:
            right -= 1
        if right - left <= 1:
            return True
        if right - left >= 4:
            return False
        nums_part = nums[left : right + 1]
        for i in range(right + 1 - left):
            previous = nums_part[i]
            nums_part[i] = nums_part[i-1] if i > 0 else float('-inf')
            if ascending(nums_part):
                return True
            nums_part[i] = previous
        return False