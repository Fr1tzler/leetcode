def countSort(nums):
    new_list = []

    while len(nums) != 0:
        new_list.append(min(nums))
        nums.pop(nums.index(min(nums)))

    return new_list


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        def find_triplets(target, left, triplets):
            right = len(nums)-1
            
            while left < right:
                if nums[left] + nums[right] == target:
                    triplets.append([-target, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif nums[left] + nums[right] > target:
                    right -= 1
                
                else:
                    left += 1

        nums = countSort(nums)
        triplets = []

        for index in range(len(nums)):
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            else:
                find_triplets(-nums[index], index + 1, triplets)

        return triplets
