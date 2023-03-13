class Solution:
    def dfs(self, i, j, prevHeight, heights, vis):
        if (i, j) in vis or i < 0 or i > len(heights) - 1 or j < 0 or j > len(heights[0]) - 1 or heights[i][j] < prevHeight:
            return
        
        vis.add((i, j))
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        for dr, dc in directions:
            ni, nj = i + dr, j + dc
            
            self.dfs(ni, nj, heights[i][j], heights, vis)
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        
        pac, atl = set(), set()
        
        for i in range(cols):
            self.dfs(0, i, heights[0][i], heights, pac)
            self.dfs(rows - 1, i, heights[rows - 1][i], heights, atl)
            
        for i in range(rows):
            self.dfs(i, 0, heights[i][0], heights, pac)
            self.dfs(i, cols - 1, heights[i][cols - 1], heights, atl)
            
        res = []
        
        for i in range(rows):
            for j in range(cols):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
                    
        return res