class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        matrixSum = 0
        
        for i in range(len(mat)):
            matrixSum += mat[i][i]
            
        for i in range(len(mat)):
            matrixSum += mat[i][len(mat) - i - 1]
        
        if len(mat) % 2 != 0:
            matrixSum -= mat[len(mat) // 2][len(mat) // 2]
            
        return matrixSum
                