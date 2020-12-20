class Solution(object):
    def minDeletionSize(self, A):
        res = 0
        for col_id in range(len(A[0])):
            column = [A[x][col_id] for x in range(len(A))]
            for i in range(1, len(column)):
                if column[i] < column[i - 1]:
                    res += 1
                    break
        return res