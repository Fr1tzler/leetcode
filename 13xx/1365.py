class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        counting_dict = dict()
        current = sorted_nums[0] - 1
        for i in range(len(sorted_nums)):
            if sorted_nums[i] != current:
                counting_dict[sorted_nums[i]] = i
                current = sorted_nums[i]
        result = []
        for i in nums:
            result.append(counting_dict[i])
        return result