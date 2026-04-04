class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        queue.append((0, 0))
        visit.add((0, 0))
        length = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if min(nr, nc) < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == 1 or (nr, nc) in visit:
                        continue
                    queue.append((nr, nc))
                    visit.add((nr, nc))
            length += 1
        return -1