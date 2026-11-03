from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        num_islands = 0

        def bfs(r, c):
            deq = deque()
            grid[r][c] = "2"
            deq.append((r,c))

            while deq:
                row, col = deq.popleft()
                for dx, dy in directions:
                    x, y = row + dx, col + dy
                    if (0 <= x < rows) and (0 <= y < cols) and grid[x][y] == "1":
                        deq.append((x, y))
                        grid[x][y] = "2"

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    bfs(i, j)
                    num_islands += 1

        return num_islands


        