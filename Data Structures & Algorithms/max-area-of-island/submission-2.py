class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        row, col = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        maxIsland = 0

        def dfs(r, c):

            grid[r][c] = -1
            count = 1

            for dx, dy in directions:
                x, y = r + dx, c + dy
                if x in range(row) and y in range(col) and grid[x][y] == 1:
                    grid[x][y] = -1
                    count += dfs(x, y)

            return count


        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    currSize = dfs(i, j)
                    maxIsland = max(maxIsland, currSize)

        return maxIsland

        