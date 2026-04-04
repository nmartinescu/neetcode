class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        maximum = 0
        dp = [0] * (m + 1)
        prev = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == '1':
                    dp[j] = min(dp[j - 1], prev, dp[j]) + 1
                else:
                    dp[j] = 0
                prev = temp
                maximum = max(maximum, dp[j])
        return maximum * maximum