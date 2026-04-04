class Solution:
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        cache = [[0] * m for i in range(n)]
        def dp(i, j):
            if i == n or j == m or obstacleGrid[i][j]:
                return 0
            elif cache[i][j]:
                return cache[i][j]
            elif i == n - 1 and j == m - 1:
                return 1 - obstacleGrid[i][j]
            else:
                cache[i][j] = dp(i + 1, j) + dp(i, j + 1)
                return cache[i][j]

        return dp(0, 0)