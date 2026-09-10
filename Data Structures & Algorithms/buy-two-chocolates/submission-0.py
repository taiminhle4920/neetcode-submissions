class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        if len(prices) < 2:
            return money
        prices.sort()
        temp = money -prices[0] - prices[1]
        return temp if temp>=0 else money
