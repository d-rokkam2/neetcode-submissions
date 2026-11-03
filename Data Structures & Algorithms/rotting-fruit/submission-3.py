from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        dq = deque()
        ROWS, COLS = len(grid),len(grid[0])
        fresh = time = 0


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    dq.append((i,j))

        if fresh == 0:
            return 0

        # bfs
        while dq and fresh > 0:
            for _ in range(len(dq)):
                r, c = dq.popleft()
                for dx, dy in directions:
                    x, y = r + dx, c + dy
                    if 0 <= x < ROWS and 0 <= y < COLS and grid[x][y] == 1:
                        dq.append((x,y))
                        grid[x][y] = 2
                        fresh -= 1

            time += 1
        return time if fresh == 0 else -1









