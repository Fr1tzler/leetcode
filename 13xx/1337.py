class Solution(object):
    def kWeakestRows(self, mat, k):
        processed_map = [[mat[i], i] for i in range(len(mat))]
        processed_map.sort(key=lambda elem: sum(elem[0]))
        return [processed_map[i][1] for i in range(k)]