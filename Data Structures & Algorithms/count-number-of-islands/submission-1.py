class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        n = len(grid)
        m = len(grid[0])
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        count = 0

        def dfs(r, c):

            grid[r][c] = "2"

            for dx, dy in directions:
                x, y = r + dx, c + dy
                if (x >= 0 and y >= 0 and y < m and x < n and grid[x][y] == "1"):
                    dfs(x, y)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1

        return count
        