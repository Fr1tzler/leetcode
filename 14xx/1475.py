class Solution(object):
    def finalPrices(self, prices):
        for good_id in range(len(prices) - 1):
            for other_id in range(good_id + 1, len(prices)):
                if prices[other_id] <= prices[good_id]:
                    prices[good_id] -= prices[other_id]
                    break
        return prices