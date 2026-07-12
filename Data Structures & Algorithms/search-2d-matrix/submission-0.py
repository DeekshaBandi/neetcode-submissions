class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        
        left = 0
        right = row * col - 1
        while left <= right:
            m = left + (right - left) // 2
            row, cols = m // col, m % col
            if target > matrix[row][cols]:
                left = m + 1
            elif target < matrix[row][cols]:
                right = m - 1
            else:
                return True 
        return False
