class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        max_area = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def dfs(r, c):
            grid[r][c] = -1
            curr = 1
            for dx, dy in directions:
                x, y = r + dx, c + dy
                if x in range(ROWS) and y in range(COLS) and grid[x][y] == 1:
                    curr += dfs(x, y)
                    grid[x][y] = -1

            return curr

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    curr_area = dfs(i, j)
                    max_area = max(max_area, curr_area)

        return max_area
        