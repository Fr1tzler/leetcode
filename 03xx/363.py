import bisect

class Solution:
    def maxSumSubmatrix(self, matrix, k):
        def get_prefix_sum(ary):
            n = len(ary)
            pre_sum = [ary[0]] * n
            for i in range(1,n):
                pre_sum[i] = pre_sum[i-1] + ary[i]
            return pre_sum

        def sum_row(matrix, c1, c2):
            ary = []
            for r in range(len(matrix)):
                res = 0
                for c in range(c1,c2+1):
                    res += matrix[r][c]
                ary.append(res)
            return ary

        def max_subarray_less_k(ary, k):
            prefix_sum = get_prefix_sum(ary)
            res = float('-inf')
            prefix_sum = [0] + prefix_sum
            n = len(prefix_sum)
            
            prefix_ascd = [0]
            for i in range(1,n):
                if prefix_sum[i] == k:
                    return k
                idx = bisect.bisect_left(prefix_ascd, prefix_sum[i] - k)
                if 0 <= idx < len(prefix_ascd):
                    res = max(res, prefix_sum[i] - prefix_ascd[idx])
                bisect.insort(prefix_ascd, prefix_sum[i])
            return res
                
        row_count = len(matrix)
        column_count = len(matrix[0])
        res = float('-inf')
        for c1 in range(column_count):
            for c2 in range(c1,column_count):
                ary = sum_row(matrix, c1, c2)
                res = max(res, max_subarray_less_k(ary,k))
        return res