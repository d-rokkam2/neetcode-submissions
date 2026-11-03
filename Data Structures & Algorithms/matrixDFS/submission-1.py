class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        seen = set()

        def dfs(r, c):
            paths = 0
            
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return 0

            if grid[r][c] == 1 or (r,c) in seen:
                return 0

            if r == ROWS - 1 and c == COLS - 1:
                return 1

            seen.add((r,c))
            for dx, dy in directions:
                x, y = r + dx, c + dy
                paths += dfs(x, y)
            seen.remove((r,c))
                
            return paths

        return dfs(0,0)
        