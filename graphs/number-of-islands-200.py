class Solution:
    def numberOfIslands(self, grid: List[List[str]]) -> int:
        count = 0

        self.grid = grid
        self.ROWS = len(grid)
        self.COLS = len(grid[0])

        for r in range(self.ROWS):
            for c in range(self.COLS):
                if(grid[r][c] == "1"):
                    count += 1
                    self.dfs(r, c)

        return count

    def dfs(self, row, col):
        if(row < 0 or row >= self.ROWS or col < 0 or col >= self.COLS):
            return

        if(self.isValid(self.grid, row, col)):
            self.grid[row][col] = "2"
            self.dfs(row-1, col)
            self.dfs(row+1, col)
            self.dfs(row, col-1)
            self.dfs(row, col+1)

    def isValid(self, row, col):
        if(self.grid[row][col] == "1"):
            return True

        return False
