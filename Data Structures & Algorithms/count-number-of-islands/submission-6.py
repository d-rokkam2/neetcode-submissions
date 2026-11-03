class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        num_islands = 0

        def dfs(i, j):
            grid[i][j] == '#'
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < ROWS and 0 <= y < COLS and grid[x][y] == '1':
                    grid[x][y] = '#'
                    dfs(x,y)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    dfs(i, j)    
                    num_islands += 1

        return num_islands