class Solution:
    def trimMean(self, arr):
        numToRemove = len(arr) // 20
        for i in range(numToRemove):
            arr.remove(max(arr))
            arr.remove(min(arr))
        return float(sum(arr))   / len(arr)