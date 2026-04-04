class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        dp, n, m = costs[0], len(costs), len(costs[0])
        for i in range(1, n):
            min1, min2, min1_index = -1, -1, -1
            for j in range(m):
                if min1 == -1 or dp[j] < min1:
                    min2 = min1
                    min1 = dp[j]
                    min1_index = j
                elif min2 == -1 or dp[j] < min2:
                    min2 = dp[j]
                
            for j in range(m):
                dp[j] = costs[i][j] + (min2 if j == min1_index else min1)
        return min(dp)