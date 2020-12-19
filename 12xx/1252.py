class Solution(object):
    def oddCells(self, n, m, indices):
        def increment_row(matrix, row_id):
            for column_id in range(len(matrix[row_id])):
                matrix[row_id][column_id] += 1
        
        def increment_column(matrix, column_id):
            for row_id in range(len(matrix)):
                matrix[row_id][column_id] += 1

        def count_odd_numbers(matrix):
            result = 0
            for row in matrix:
                for cell in row:
                    if cell % 2 == 1:
                        result += 1
            return result

        matrix = [[0] * m for indice in range(n)]
        for indice in indices:
            increment_row(matrix, indice[0])
            increment_column(matrix, indice[1])
        return count_odd_numbers(matrix)