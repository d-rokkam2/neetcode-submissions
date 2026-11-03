class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):

                curr = board[i][j]
                box_index = (i // 3) * 3 + (j // 3)
                if curr == '.':
                    continue

                if curr in boxes[box_index] or curr in rows[i] or curr in cols[j]:
                    return False

                rows[i].add(curr)
                cols[j].add(curr)
                boxes[box_index].add(curr)

        return True

                










        