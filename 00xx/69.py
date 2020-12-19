class Solution(object):
    def mySqrt(self, x):
        left = 0
        right = x + 1
        middle = (left + right) // 2
        while not(middle * middle <= x < (middle + 1) * (middle + 1)):
            if middle * middle < x:
                left = middle
            if middle * middle > x:
                right = middle
            middle = (left + right) // 2
        return middle
