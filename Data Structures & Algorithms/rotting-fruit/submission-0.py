class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        visit = set()
        queue = deque()
        fruit = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visit.add((i, j))
                if grid[i][j]:
                    fruit += 1
        length = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                fruit -= 1
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if min(nr, nc) < 0 or nr == ROWS or nc == COLS or (nr, nc) in visit or grid[nr][nc] != 1:
                        continue
                    queue.append((nr, nc))
                    visit.add((nr, nc))
            if len(queue):
                length += 1
        return -1 if fruit != 0 else length