class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix:
            return False

        ROWS, COLS = len(matrix), len(matrix[0])
        bot, top = 0, ROWS - 1
        found_row = None

        while bot <= top:
            m = (bot + top) // 2
            if matrix[m][-1] < target:
                bot = m + 1
            elif matrix[m][0] > target:
                top = m - 1
            else:
                found_row = m
                break

        if found_row == None:
            return False

        l, r = 0, COLS - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[found_row][mid] == target:
                return True
            elif matrix[found_row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False



        
