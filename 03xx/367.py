class Solution(object):
    def isPerfectSquare(self, num):
        left = 1
        right = 2 ** 16
        middle = (left + right) // 2
        while not middle * middle <= num < (middle + 1) * (middle + 1):
            if middle * middle > num:
                right = middle
            else:
                left = middle
            middle = (left + right) // 2
        return middle * middle == num