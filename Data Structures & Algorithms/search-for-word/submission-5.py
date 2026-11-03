from collections import deque
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        directions = [(1,0), (0,1),(-1,0),(0,-1)]
        ROWS, COLS = len(board), len(board[0])
        seen = set()

        def dfs(r, c, index):

            if index == len(word):
                return True

            temp = board[r][c]
            board[r][c] = '-1'

            for dx, dy in directions:
                x, y = r + dx, c + dy
                if 0 <= x < ROWS and 0 <= y < COLS and board[x][y] == word[index]:
                    if dfs(x, y, index + 1):
                        return True
                        
            board[r][c] = temp

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0] and board[i][j] != '-1':
                    if dfs(i, j, 1):
                        return True
        
        return False

        