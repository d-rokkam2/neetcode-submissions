class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        seen = set()
        islandCount = 0

        def dfs(r, c):
            seen.add((r,c))
            for dx, dy in directions:
                x, y = r + dx, c + dy
                if (0 <= x < ROWS) and (0 <= y < COLS) and (grid[x][y] == '1') and ((x, y) not in seen):
                    seen.add((x,y))
                    dfs(x, y)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1' and (i,j) not in seen:
                    dfs(i, j)
                    islandCount += 1
                    
        return islandCount

        