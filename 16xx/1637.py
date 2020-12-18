class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        points.sort(key=lambda x: x[0])
        return max([points[i] - points[i-1] for i in range(1, len(points))])