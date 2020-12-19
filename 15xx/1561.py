class Solution(object):
    def maxCoins(self, piles):
        piles.sort()
        total_len = len(piles)
        piles = piles[total_len // 3:]
        print(piles)
        return sum([piles[i] for i in range(0, len(piles), 2)])
