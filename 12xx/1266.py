class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        result = 0
        for i in range(1, len(points)):
            dx, dy = points[i][0] - points[i - 1][0], points[i][1] - points[i - 1][1]
            result += max(abs(dx), abs(dy))
        return result