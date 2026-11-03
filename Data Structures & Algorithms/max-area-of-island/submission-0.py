from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        rows, cols = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        bigIsland = 0

        def dfs(r, c):

            grid[r][c] = -1
            currentSize = 1

            for dx, dy in directions:
                x, y = r + dx, c + dy
                if x in range(rows) and y in range(cols) and grid[x][y] == 1:
                    grid[x][y] = -1
                    currentSize += dfs(x, y)
                    

            return currentSize


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    currSize = dfs(i, j)
                    bigIsland = max(bigIsland, currSize)

        return bigIsland


        
        