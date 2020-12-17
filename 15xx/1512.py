class Solution(object):
    def numIdenticalPairs(self, nums):
        counting_dict = dict()
        for i in range(len(nums)):
            if nums[i] in counting_dict:
                counting_dict[nums[i]].append(i)
            else:
                counting_dict[nums[i]] = [i]
        result = 0
        for i in counting_dict:
            l = len(counting_dict[i])
            result += l * (l - 1) // 2
        return result
