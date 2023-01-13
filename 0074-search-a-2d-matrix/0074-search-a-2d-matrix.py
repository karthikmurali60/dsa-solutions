class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        topRow, bottomRow = 0, rows - 1
        
        while topRow <= bottomRow:
            midRow = int(topRow + ((bottomRow - topRow) / 2))
            
            if target > matrix[midRow][-1]:
                topRow = midRow + 1
            elif target < matrix[midRow][0]:
                bottomRow = midRow - 1
            else:
                break
                                
        # Element not present        
        if topRow > bottomRow:
            return False
            
        targetRow = int(topRow + ((bottomRow - topRow) / 2))
        left, right = 0, cols - 1
        
        while left <= right:
            mid = int(left + ((right - left) / 2))
            
            if target == matrix[targetRow][mid]:
                return True
            elif target > matrix[targetRow][mid]:
                left = mid + 1
            else:
                right = mid - 1
                
        return False