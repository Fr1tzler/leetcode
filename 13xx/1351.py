class Solution(object):
    def countNegatives(self, grid):
        def binsearch(row):
            if row[0] < 0:
                return len(row)
            if row[-1] >= 0:
                return 0
            left = 0
            right = len(row) - 1
            middle = (left + right) // 2
            while left < right - 1:
                if row[middle] >= 0:
                    left = middle
                else:
                    right = middle
                middle = (left + right) // 2
            return len(row) - middle - 1
        
        res = 0
        for row in grid:
            res += binsearch(row)
        return res
