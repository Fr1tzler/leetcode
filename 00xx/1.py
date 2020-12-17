class Solution(object):
    def twoSum(self, nums, target):
        arr = [[nums[i], i] for i in range(len(nums))]
        arr.sort(key=lambda x : x[0])
        i, j = 0, len(arr) - 1
        while(i < j):
            if arr[i][0] + arr[j][0] < target:
                i += 1
            elif arr[i][0] + arr[j][0] > target:
                j -= 1
            else:
                return sorted([arr[i][1], arr[j][1]])