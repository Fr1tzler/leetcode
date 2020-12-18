class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        res = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if (j - i) % 2 == 0:
                    res += sum(arr[i : j + 1])
        return res
