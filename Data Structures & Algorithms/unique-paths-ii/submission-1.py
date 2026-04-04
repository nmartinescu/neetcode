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

        prevRow = [0] * m
        prevRow[m - 1] = 1
        for i in range(n - 1, -1, -1):
            currRow = [0] * m
            currRow[m - 1] = 1 if not obstacleGrid[i][m - 1] and prevRow[m - 1] else 0
            for j in range(m - 2, -1, -1):
                currRow[j] = 0 if obstacleGrid[i][j] else currRow[j + 1] + prevRow[j]
            prevRow = currRow
        return prevRow[0]