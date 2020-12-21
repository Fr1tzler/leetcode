class Solution(object):
    def constructRectangle(self, area):
        for w in range(1, area + 1):
            if area % w == 0:
                if area // w <= w:
                    return [w, area // w]