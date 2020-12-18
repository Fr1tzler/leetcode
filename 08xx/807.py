class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        row_maxes = []
        column_maxes = [0 for i in range(len(grid[0]))]
        for row in grid:
            row_maxes.append(max(row))
            for column in range(len(row)):
                column_maxes[column] = max(column_maxes[column], row[column])
        result = 0
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                result += min(row_maxes[row], column_maxes[column]) - grid[row][column]
        return result
        