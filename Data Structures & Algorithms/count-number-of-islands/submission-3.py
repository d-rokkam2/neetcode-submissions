class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        res = 0
        row, col = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def dfs(r, c):

            grid[r][c] = "2"

            for dx, dy in directions:
                x, y = r + dx, c + dy
                if x in range(row) and y in range(col) and grid[x][y] == "1":
                    grid[x][y] = "2"
                    dfs(x, y)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1

        return res

        