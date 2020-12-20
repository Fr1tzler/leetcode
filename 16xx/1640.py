class Solution(object):
    def canFormArray(self, arr, pieces):
        for piece in pieces:
            for num in piece:
                if num not in arr:
                    return False
            for i in range(1, len(piece)):
                if arr.index(piece[i - 1]) + 1 != arr.index(piece[i]):
                    return False
        return True
