#User function Template for python3

class Solution:
    def dfs(self, i, j, n, m, mat, vis):
        # print("--------")
        vis[i][j] = 1
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        for dr, dc in directions:
            nr, nc = dr + i, dc + j
            
            if nr < 0 or nr > n - 1 or nc < 0 or nc > m - 1 or vis[nr][nc] == 1 or mat[nr][nc] == 'X':
                continue
            
            # print(nr, nc)
            self.dfs(nr, nc, n, m, mat, vis)
            
        
        
    def fill(self, n, m, mat):
        # code here
        
        vis = [[0] * m for i in range(n)]
        # print(vis)
        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n-1 or j == 0 or j == m-1) and mat[i][j] == 'O':
                    # print(i, j)
                    self.dfs(i, j, n, m, mat, vis)
                    
        # print(vis)
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 'O' and vis[i][j] == 0:
                    mat[i][j] = 'X'
                    
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