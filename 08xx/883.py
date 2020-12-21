class Solution(object):
    def projectionArea(self, grid):
        result = 0
        zero_count = 0
        for row_id in range(len(grid)):
            result += max(grid[row_id])
            zero_count += grid[row_id].count(0)
        for column_id in range(len(grid[0])):
            result += max([grid[row_id][column_id] for row_id in range(len(grid))])
        return result + len(grid) * len(grid[0]) - zero_count