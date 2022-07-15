class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        self.BOARD = board
        self.ROWS = len(board)
        self.COLS = len(board[0])

        for r in range(self.ROWS):
            for c in range(self.COLS):
                if(r == 0 or r == (self.ROWS - 1) or c == 0 or c == (self.COLS - 1)):
                    self.dfs(r, c)

        for r in range(self.ROWS):
            for c in range(self.COLS):
                if(board[r][c] == "O"):
                    board[r][c] = "X"
                if(board[r][c] == "E"):
                    board[r][c] = "O"


    def dfs(self, row, col):
        if(row < 0 or row >= self.ROWS or col < 0 or col >= self.COLS or self.BOARD[row][col] != "O"):
            return

        self.BOARD[row][col] = "E"
        self.dfs(row-1, col)
        self.dfs(row+1, col)
        self.dfs(row, col-1)
        self.dfs(row, col+1)
