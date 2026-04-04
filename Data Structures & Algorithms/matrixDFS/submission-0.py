class Solution:
    def dfs(self, grid: List[List[int]], r: int, c: int, visits: Set) -> int:
        ROW_MAX, COL_MAX = len(grid), len(grid[0])
        if min(r, c) < 0 or r == ROW_MAX or c == COL_MAX or (r, c) in visits or grid[r][c] == 1:
            return 0
        if r == ROW_MAX - 1 and c == COL_MAX - 1:
            return 1
        visits.add((r, c))
        count = 0
        count += self.dfs(grid, r - 1, c, visits)
        count += self.dfs(grid, r, c - 1, visits)
        count += self.dfs(grid, r + 1, c, visits)
        count += self.dfs(grid, r, c + 1, visits)
        visits.remove((r, c))
        return count

    def countPaths(self, grid: List[List[int]]) -> int:
        return self.dfs(grid, 0, 0, set())