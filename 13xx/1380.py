class Solution(object):
    def luckyNumbers (self, matrix):
        row_min = [min(row) for row in matrix]
        col_max = []
        for column_id in range(len(matrix[0])):
            column = [matrix[row_id][column_id] for row_id in range(len(matrix))]
            col_max.append(max(column))
        return list(set(row_min).intersection(set(col_max)))