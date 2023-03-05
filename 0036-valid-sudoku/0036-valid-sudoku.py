class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:        
        
        # Check for each row
        for i in range(len(board)):
            hashSet = set()
            
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                
                if board[i][j] in hashSet:
                    return False
                
                hashSet.add(board[i][j])
                
        # Check for each column
        for j in range(len(board[0])):
            hashSet = set()
            
            for i in range(len(board)):
                if board[i][j] == ".":
                    continue
                
                if board[i][j] in hashSet:
                    return False
                
                hashSet.add(board[i][j])
                
        # Check for each 3x3 grid
        hashMap = {}
        for i in range(3):
            for j in range(3):
                hashMap[(i, j)] = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                    
                if board[i][j] in hashMap[(i // 3, j // 3)]:
                    return False

                hashMap[(i // 3, j // 3)].add(board[i][j])
                
        return True