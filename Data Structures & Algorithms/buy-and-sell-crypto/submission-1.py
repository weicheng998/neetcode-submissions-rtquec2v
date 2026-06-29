class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        max_profit = 0
        for p in prices:
            profit = p - min_buy
            max_profit = max(max_profit, profit)
            min_buy = min(min_buy, p)
        return max_profit
