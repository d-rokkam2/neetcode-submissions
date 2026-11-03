from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (0,-1),(-1,0)]
        maxArea = 0

        def bfs(r, c):
            deq = deque()
            deq.append((r, c))
            count = 0

            grid[r][c] = -1

            while deq:
                row, col = deq.popleft()
                count += 1
                for dx, dy in directions:
                    x, y = dx + row, dy + col
                    if x in range(rows) and y in range(cols) and grid[x][y] == 1:
                        grid[x][y] = -1
                        deq.append((x,y))

            return count

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    currentArea = bfs(i, j)
                    maxArea = max(maxArea, currentArea)

        return maxArea
        