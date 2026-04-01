class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        profit = 0

        for p in prices:
            min_price = min(p, min_price)
            profit = max(p - min_price, profit)

        return profit
        