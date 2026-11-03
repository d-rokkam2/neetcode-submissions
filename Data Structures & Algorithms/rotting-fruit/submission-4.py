from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        freshCount = time = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        dq = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    freshCount += 1
                if grid[i][j] == 2:
                    dq.append((i,j))
                continue

        if freshCount == 0:
            return 0

        while dq and freshCount > 0:
            for _ in range(len(dq)):
                r, c = dq.popleft()
                for dx, dy in directions:
                    x, y = r + dx, c + dy
                    if 0 <= x < ROWS and 0 <= y < COLS and grid[x][y] == 1:
                        grid[x][y] = 2
                        dq.append((x,y))
                        freshCount -= 1
            
            time += 1

        return time if freshCount == 0 else -1






            

    

        