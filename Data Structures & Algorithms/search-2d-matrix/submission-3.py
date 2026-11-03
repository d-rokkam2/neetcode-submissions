class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix:
            return False
        
        n = len(matrix) 
        m = len(matrix[0]) 

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == target:
                    return True
        return False

        