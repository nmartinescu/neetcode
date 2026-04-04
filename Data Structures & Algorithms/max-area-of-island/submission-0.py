class Solution:
    def dfs(self, grid: List[List[int]], r: int, c: int) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
            return 0
        grid[r][c] = 0
        size = 1
        size += self.dfs(grid, r - 1, c)
        size += self.dfs(grid, r, c - 1)
        size += self.dfs(grid, r + 1, c)
        size += self.dfs(grid, r, c + 1)
        return size

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maximum_size = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]:
                    maximum_size = max(maximum_size, self.dfs(grid, i, j))
        return maximum_size