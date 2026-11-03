class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n = len(board)
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(n):
            for j in range(n):

                curr_square = board[i][j]
                box_index = (i // 3) * 3 + (j // 3)

                if curr_square == ".":
                    continue
                
                if (curr_square in rows[i]) or (curr_square in cols[j]) or (curr_square in boxes[box_index]):
                   return False
                
                rows[i].add(curr_square)
                cols[j].add(curr_square)
                boxes[box_index].add(curr_square)

        return True







        