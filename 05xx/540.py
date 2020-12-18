class Solution(object):
    def singleNonDuplicate(self, nums):
        if len(nums) == 1:
            return nums[0]
        middle = (len(nums) - 1) // 2
        if middle % 2 == 0:
            if nums[middle] != nums[middle + 1]:
                return self.singleNonDuplicate(nums[ : middle + 1])
            return self.singleNonDuplicate(nums[middle : ])
        else:
            if nums[middle] != nums[middle - 1]:
                return self.singleNonDuplicate(nums[ : middle])
            return self.singleNonDuplicate(nums[middle + 1 : ])
