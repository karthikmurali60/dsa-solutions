class Solution:

    #Function to find minimum time required to rot all oranges. 
	def orangesRotting(self, grid):
		#Code here
		
        # We will use BFS for this problem.
        
        m, n = len(grid), len(grid[0])
        
        vis = [[0] * n for _ in range(m)]
        
        queue = []
        
        minTime = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    vis[i][j] = 2
                    queue.append([i, j , 0])
                    
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                    
        while queue:
            row, col, time = queue.pop(0)
            
            minTime = max(minTime, time)
            
            for di, dj in directions:
                ni, nj = row + di, col + dj
                
                if ni < 0 or ni >= m or nj < 0 or nj >= n or vis[ni][nj] == 2 or grid[ni][nj] != 1:
                    continue
                
                grid[ni][nj] = 2
                vis[ni][nj] = 2
                
                queue.append([ni, nj, time + 1])
            
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
                    
        return minTime
            


#{ 
 # Driver Code Starts
from queue import Queue

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.orangesRotting(grid)
		print(ans)

# } Driver Code Ends