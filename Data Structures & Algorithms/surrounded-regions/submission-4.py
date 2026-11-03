class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS, COLS = len(board), len(board[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def capture(r, c):
            board[r][c] = 'T'
            for dx, dy in directions:
                x, y = r + dx, c + dy
                if 0 <= x < ROWS and 0 <= y < COLS and board[x][y] == 'O':  
                    capture(x,y)


        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O' and (i in (0,ROWS-1) or j in (0, COLS-1)):
                    capture(i, j)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'T':
                    board[i][j] = 'O'