class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        def is_arithmetic(nums):
            if len(nums) <= 2:
                return True
            nums.sort()
            delta = nums[0] - nums[1]
            for i in range(1, len(nums) - 1):
                if nums[i] - nums[i + 1] != delta:
                    return False
            return True
        
        result = []
        for i in range(len(l)):
            result.append(is_arithmetic(nums[l[i] : r[i] + 1]))
        return result