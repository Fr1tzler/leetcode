class Solution(object):
    def islandPerimeter(self, grid):
        row_count = len(grid)
        col_count = len(grid[0])
        processed_map = [[0] * (col_count + 2) for i in range(row_count + 2)]
        for x in range(row_count):
            for y in range(col_count):
                processed_map[x + 1][y + 1] = grid[x][y]
        result = 0
        for x in range(row_count):
            for y in range(col_count):
                if processed_map[x + 1][y + 1] != 1:
                    continue
                if processed_map[x + 1][y + 1] != processed_map[x][y + 1]:
                    result += 1
                if processed_map[x + 1][y + 1] != processed_map[x + 2][y + 1]:
                    result += 1
                if processed_map[x + 1][y + 1] != processed_map[x + 1][y]:
                    result += 1
                if processed_map[x + 1][y + 1] != processed_map[x + 1][y + 2]:
                    result += 1
        return result