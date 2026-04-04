class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maximum = prices[n - 1]
        max_profit = 0
        for i in range(n - 2, -1, -1):
            max_profit = max(max_profit, maximum - prices[i])
            maximum = max(maximum, prices[i])
        return max_profit