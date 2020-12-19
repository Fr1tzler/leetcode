class Solution(object):
    def diagonalSort(self, mat):
        for row_id in range(len(mat)):
            mat[row_id] = [0 for i in range(len(mat) - row_id - 1)] + mat[row_id] + [101 for i in range(row_id)]
        for column_id in range(len(mat[0])):
            column = [mat[row_id][column_id] for row_id in range(len(mat))]
            column.sort()
            for row_id in range(len(mat)):
                mat[row_id][column_id] = column[row_id]
        for row_id in range(len(mat)):
            mat[row_id] = mat[row_id][len(mat) - row_id - 1 : len(mat[row_id])  - row_id]
        return mat