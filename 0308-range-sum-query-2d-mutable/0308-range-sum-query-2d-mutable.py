class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        
        self.dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.dp[i][j + 1] = self.dp[i][j] + matrix[i][j]
                

    def update(self, row: int, col: int, val: int) -> None:
        self.matrix[row][col] = val
        
        for j in range(len(self.matrix[0])):
            self.dp[row][j + 1] = self.dp[row][j] + self.matrix[row][j]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        
        for i in range(row1, row2 + 1):
            total += self.dp[i][col2 + 1] - self.dp[i][col1]
            
        return total
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)