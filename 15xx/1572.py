class Solution(object):
    def diagonalSum(self, mat):
        l = len(mat)
        result = 0
        for i in range(l):
            result += mat[i][i] + mat[i][l - i - 1]
        if l % 2 == 1:
            result -= mat[l // 2][l // 2]
        return result
