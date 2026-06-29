class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lowest = prices[0]
        for price in prices:
            if lowest > price:
                lowest = price
            res = max(res, price - lowest)
        return res