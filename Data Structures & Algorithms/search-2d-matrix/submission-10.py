class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix:
            return False

        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS - 1
        selected_row = None

        while l <= r:
            curr = (l + r) // 2
            if target > matrix[curr][-1]:
                l = curr + 1
            elif target < matrix[curr][0]:
                r = curr - 1
            else:
                selected_row = curr
                break
        
        if selected_row == None:
            return False

        left, right = 0, COLS-1 

        while left <= right:
            mid = (left + right) // 2
            if target == matrix[selected_row][mid]:
                return True
            elif target > matrix[selected_row][mid]:
                left = mid + 1
            else:
                right = mid - 1

        return False
            