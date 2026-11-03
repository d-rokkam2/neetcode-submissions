from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        n = len(board)

        for i in range(n):
            for j in range(len(board[0])):
                curr = board[i][j]
                if curr == ".":
                    continue
                box_index = (i // 3)*3 + (j // 3)
                if curr in boxes[box_index]:
                    return False
                elif curr in rows[i] or curr in cols[j]:
                    return False

                rows[i].add(curr)
                cols[j].add(curr)
                boxes[box_index].add(curr)

        return True
               

                

        