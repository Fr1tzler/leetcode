class Solution(object):
    def replaceElements(self, arr):
        maximum = arr[-1]
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] <= maximum:
                arr[i] = maximum
            else:
                temp = maximum
                maximum = arr[i]
                arr[i] = temp
        arr[-1] = -1
        return arr