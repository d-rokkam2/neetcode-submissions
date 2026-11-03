class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        maxArea = 0
        seen = set()
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(r, c):
            seen.add((r,c))
            area = 1
            for dx, dy in directions:
                x, y = r + dx, c + dy
                if (0 <= x < ROWS) and (0 <= y < COLS) and grid[x][y] == 1 and (x,y) not in seen:
                    seen.add((x,y))
                    area += dfs(x, y)
                
            return area

        for i in range(ROWS):
            for j in range(COLS): 
                if grid[i][j] == 1 and (i, j) not in seen:
                    currArea = dfs(i, j)
                    maxArea = max(currArea, maxArea)

        return maxArea


        