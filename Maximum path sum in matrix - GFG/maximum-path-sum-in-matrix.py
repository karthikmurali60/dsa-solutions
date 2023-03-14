#User function Template for python3

class Solution:
    def dfs(self, i, j, N, Matrix, dp):
        if i < 0 or i >= N or j < 0 or j >= N:
            return -1e9
        
        if i == N - 1:
            return Matrix[i][j]
            
        if dp[i][j] != -1:
            return dp[i][j]
            
        bottom = Matrix[i][j] + self.dfs(i + 1, j, N, Matrix, dp)
        bottomLeft = Matrix[i][j] + self.dfs(i + 1, j - 1, N, Matrix, dp)
        bottomRight = Matrix[i][j] + self.dfs(i + 1, j + 1, N, Matrix, dp)
        
        dp[i][j] = max(bottom, bottomLeft, bottomRight)
        
        return dp[i][j]
    
    def maximumPath(self, N, Matrix):
        # code here
        
        maxSum = -1e9
        
        dp = [[-1] * N for _ in range(N)]
        
        for j in range(N):
            maxSum = max(maxSum, self.dfs(0, j, N, Matrix, dp))
            
        return maxSum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        Matrix = [[0]*N for i in range(N)]
        for itr in range(N*N):
            Matrix[(itr//N)][itr%N] = int(arr[itr])
        
        ob = Solution()
        print(ob.maximumPath(N, Matrix))

# } Driver Code Ends