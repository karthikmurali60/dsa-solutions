class Solution:
    def dfs(self, row, col, prevHeight, heights, vis):
        if row < 0 or row > len(heights) - 1 or col < 0 or col > len(heights[0]) - 1 or (row, col) in vis or heights[row][col] < prevHeight:
            return
        
        vis.add((row, col))
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            
            self.dfs(nr, nc, heights[row][col], heights, vis)
            
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        
        rows, cols = len(heights), len(heights[0])
        
        for j in range(cols):
            self.dfs(0, j, 0, heights, pac)
            self.dfs(rows - 1, j, 0, heights, atl)
            
        for i in range(rows):
            self.dfs(i, 0, 0, heights, pac)
            self.dfs(i, cols - 1, 0, heights, atl)
            
        res = []
        for i in range(rows):
            for j in range(cols):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
                    
        return res