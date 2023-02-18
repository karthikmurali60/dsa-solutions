#User function Template for python3

class Solution:
    def dfs(self, i, j, n, m, mat, vis):
        vis[i][j] = 1
        
        mat[i][j] = 'A'
        
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            
            if ni < 0 or ni >= n or nj < 0 or nj >= m or vis[ni][nj] or mat[ni][nj] == 'X':
                continue
            
            self.dfs(ni, nj, n, m, mat, vis)
        
    def fill(self, n, m, mat):
        # code here
        
        vis = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n - 1 or j == 0 or j == m - 1) and mat[i][j] == 'O':
                    self.dfs(i, j, n, m, mat, vis)
                    
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 'O':
                    mat[i][j] = 'X'
                    
                if mat[i][j] == 'A':
                    mat[i][j] = 'O'
        
        return mat
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = []
        for i in range(n):
            s = list(map(str,input().split()))
            mat.append(s)
        
        ob = Solution()
        ans = ob.fill(n, m, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends