from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        num_islands = 0

        def bfs(i, j):
            grid[i][j] = '#'
            dq = deque()
            dq.append((i, j))
            while dq:
                r, c = dq.popleft()
                for dx, dy in directions:
                    x, y = r + dx, c + dy
                    if x in range(0, ROWS) and y in range(0, COLS) and grid[x][y] == '1':
                        grid[x][y] = '#'
                        dq.append((x,y))
                        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    bfs(i, j)    
                    num_islands += 1

        return num_islands