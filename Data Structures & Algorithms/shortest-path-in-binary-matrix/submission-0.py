class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, 1], [1, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        if not grid[0][0]:
            queue.append((0, 0, 1))
            visit.add((0, 0))
        while queue:
            r, c, length = queue.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                return length
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if min(nr, nc) < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == 1 or (nr, nc) in visit:
                    continue
                queue.append((nr, nc, length + 1))
                visit.add((nr, nc))
        return -1