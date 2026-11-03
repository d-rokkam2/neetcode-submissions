class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])
        directions = [ [1,0], [0,1], [-1, 0], [0, -1]]
        numIslands = 0
        
        def dfs(i, j):
            grid[i][j] = '#'
            for dx, dy in directions:
                x = dx + i
                y = dy + j
                if(x >= 0 and y >= 0 and x < m and y < n and grid[x][y] == "1" ):
                    dfs(x, y)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    numIslands += 1 

        return numIslands

        