class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rowHash, colHash = {}, {}
        
        for i in range(len(matrix)):
            rowHash[i] = set()
            colHash[i] = set()
            
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] in rowHash[i] or matrix[i][j] in colHash[j]:
                    return False
                
                rowHash[i].add(matrix[i][j])
                colHash[j].add(matrix[i][j])
                
        return True