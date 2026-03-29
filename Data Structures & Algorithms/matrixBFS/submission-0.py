class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        visits = set()
        queue = deque()
        queue.append((0, 0))
        visits.add((0, 0))
        length = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                for direction in directions:
                    nr = r + direction[0]
                    nc = c + direction[1]
                    if min(nr, nc) < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == 1 or (nr, nc) in visits:
                        continue
                    queue.append((nr, nc))
                    visits.add((nr, nc))
            length += 1

        return 0