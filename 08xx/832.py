class Solution(object):
    def flipAndInvertImage(self, A):
        result = []
        for row in A:
            row.reverse()
            for i in range(len(row)):
                row[i] = 1 - row[i]
            result.append(row)
        return result