from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        seen = set()

        def bfs(r, c, pathLength):
            dq = deque()
            dq.append((r,c))
            seen.add((r,c))
            pathLength += 1
            
            while dq:
                for _ in range(len(dq)):
                    row, col = dq.popleft()

                    if row == ROWS - 1 and col == COLS - 1 and grid[r][c] == 0:
                        return pathLength

                    for dx, dy in directions:
                        x, y = row + dx, col + dy
                        if (0 <= x < ROWS) and (0 <= y < COLS) and (grid[x][y] == 0)and ((x,y) not in seen):
                            dq.append((x,y))
                            seen.add((x,y))
                pathLength += 1
            return -1

        return bfs(0,0,0)
        