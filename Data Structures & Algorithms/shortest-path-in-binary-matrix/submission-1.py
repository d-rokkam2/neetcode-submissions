from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        directions = [(1,0), (0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        ROWS, COLS = len(grid), len(grid[0])

        if grid[0][0] == 1:
            return -1

        def bfs(i, j, path):
            seen = set()
            seen.add((i,j))
            dq = deque()
            dq.append((i,j))
            path += 1
            while dq:
                for _ in range(len(dq)):
                    r, c = dq.popleft()

                    if r == ROWS - 1 and c == COLS - 1:
                        return path

                    for dx, dy in directions:
                        x, y = r + dx, c + dy
                        if x in range(ROWS) and y in range(ROWS) and grid[x][y] == 0 and (x,y) not in seen:
                            dq.append((x,y))
                            seen.add((x,y))
                path += 1


            return -1

        return bfs(0,0,0)







        