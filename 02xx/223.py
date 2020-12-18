class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        A1 = max(A, E)
        C1 = min(C, G)
        B1 = max(B, F)
        D1 = min(D, H)
        h = D1 - B1
        w = C1 - A1
        intersection = w * h
        if h <= 0 or w <= 0:
            intersection = 0
        return (C - A) * (D - B) + (G - E) * (H - F) - intersection