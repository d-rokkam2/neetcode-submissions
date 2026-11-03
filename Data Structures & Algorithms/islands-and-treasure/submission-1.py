from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        INF = 2147483647

        def bfs(r, c):
            dq = deque()
            dq.append((r,c))
            steps = 0
            visit = set()
            visit.add((r,c))
            while dq:
                for _ in range(len(dq)):
                    row, col = dq.popleft()
                    if grid[row][col] == 0:
                        return steps
                    for dx, dy in directions:
                        x, y = row + dx, col + dy
                        if 0 <= x < ROWS and 0 <= y < COLS and (x,y) not in visit and grid[x][y] != -1:
                            visit.add((x,y))
                            dq.append((x,y))
                steps += 1
            return INF

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == INF:
                    grid[i][j] = bfs(i, j)


        
        