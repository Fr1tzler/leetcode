class Solution(object):
    def minCostToMoveChips(self, position):
        odd = 0
        even = 0
        for i in position:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
        return min(odd, even)