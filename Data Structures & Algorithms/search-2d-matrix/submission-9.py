class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        bottom, top = 0, ROWS - 1
        selected_row = None

        while bottom <= top:
            row = (bottom + top) // 2 
            if target > matrix[row][-1]:
                bottom = row + 1
            elif target < matrix[row][0]:
                top = row - 1
            else:
                selected_row = row
                break

        if selected_row == None:
            return False

        l, r = 0, COLS - 1
        while l <= r:
            col = (l + r) // 2
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                l = col + 1
            else:
                r = col - 1


        return False




        