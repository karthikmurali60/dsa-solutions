#User function Template for python3

class Solution:  
    def dfs(self, index, a, n, dp):
        if index == 0:
            return a[index]
            
        if index < 0:
            return 0
        
        if dp[index] != -1:
            return dp[index]
            
        pick = a[index] + self.dfs(index - 2, a, n, dp)
        notPick = self.dfs(index - 1, a, n, dp)
        
        dp[index] = max(pick, notPick)
        
        return dp[index]
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        dp = [-1] * n
        
        return self.dfs(n - 1, a, n, dp)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.FindMaxSum(a,n))
# } Driver Code Ends