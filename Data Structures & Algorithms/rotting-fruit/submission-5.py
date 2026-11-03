from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        fresh = time = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        dq = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    dq.append((i,j))


        if fresh == 0:
            return 0

        while dq and fresh > 0:
            for _ in range(len(dq)):
                row, col = dq.popleft()
                for dx, dy in directions:
                    x, y = row + dx, col + dy
                    if 0 <= x < ROWS and 0 <= y < COLS and grid[x][y] == 1:
                        grid[x][y] = 2
                        dq.append((x, y))
                        fresh -=1 
            time += 1

        return time if fresh == 0 else -1
                    




    

        