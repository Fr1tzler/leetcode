class Solution(object):
    def processQueries(self, queries, m):
        permutation = list(range(m, 0, -1))
        for i in range(len(queries)):
            position = permutation.index(queries[i])
            permutation.pop(position)
            permutation.append(queries[i])
            queries[i] = m - position
        return queries