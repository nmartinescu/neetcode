class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        currMax = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            price = prices[i]
            if price < currMax:
                ans += currMax - price
            currMax = price
        return ans
            