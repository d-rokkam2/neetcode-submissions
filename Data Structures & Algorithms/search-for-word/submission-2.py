from collections import deque
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        directions = [(1,0), (0,1),(-1,0),(0,-1)]
        ROWS, COLS = len(board), len(board[0])
        seen = set()

        def dfs(r, c, index):

            if index == len(word):
                return True

            for dx, dy in directions:
                x, y = r + dx, c + dy
                if 0 <= x < ROWS and 0 <= y < COLS and board[x][y] == word[index] and (x, y) not in seen:
                    seen.add((x, y))
                    if dfs(x, y, index + 1):
                        return True
                    seen.remove((x,y))

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    seen.add((i, j))
                    if dfs(i, j, 1):
                        return True
                    seen.clear()
        
        return False

        