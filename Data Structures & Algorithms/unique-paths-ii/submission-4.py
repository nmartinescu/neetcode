class Solution:
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [0] * m
        dp[m - 1] = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if obstacleGrid[i][j]:
                    dp[j] = 0
                elif j + 1 < m:
                    dp[j] += dp[j + 1]
        return dp[0]