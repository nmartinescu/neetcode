class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [0] * m
        for i in range(n - 1, -1, -1):
            currRow = [0] * m
            currRow[m - 1] = 1
            for j in range(m - 2, -1, -1):
                currRow[j] = prevRow[j] + currRow[j + 1]
            prevRow = currRow
        return prevRow[0]