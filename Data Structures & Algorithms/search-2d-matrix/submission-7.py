class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix or not matrix[0]:
            return False

        n = len(matrix)

        for i in range(n):
            left = 0
            right = len(matrix[i]) - 1

            if matrix[i][right] < target:
                continue

            if matrix[i][0] > target:
                break

            while left <= right:

                mid = (left + right) // 2

                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

        return False



        