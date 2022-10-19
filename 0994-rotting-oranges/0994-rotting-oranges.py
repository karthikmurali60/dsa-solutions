class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        time = 0
        queue = []
        fresh = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append([i,j])
                if grid[i][j] == 1:
                    fresh += 1
                    
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                    
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.pop(0)
                
                for dr, dc in directions:
                    row = dr + r
                    col = dc + c
                    
                    if row < 0 or row > rows - 1 or col < 0 or col > cols - 1 or grid[row][col] != 1:
                        continue
                    
                    grid[row][col] = 2
                    queue.append([row, col])
                    fresh -= 1
                
            time += 1
        
        if fresh == 0:
            return time
        else:
            return -1
                
        