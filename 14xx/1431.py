class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maximum = max(candies)
        result = []
        for child in candies:
            result.append(child + extraCandies >= maximum)
        return result