class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        max_profit = 0
        for p in prices:
            profit = p - min_buy
            if profit > max_profit:
                max_profit = profit
            if p < min_buy:
                min_buy = p
        return max(max_profit, 0)
