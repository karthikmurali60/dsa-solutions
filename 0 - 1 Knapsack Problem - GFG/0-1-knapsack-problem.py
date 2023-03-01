#User function Template for python3

class Solution:
    def backtrack(self, index, W, wt, val, dp):
        if index == 0:
            if wt[index] <= W:
                return val[index]
            
            return 0
    
        if dp[index][W] != -1:
            return dp[index][W]
            
        notPick = self.backtrack(index - 1, W, wt, val, dp)
        
        pick = -float('inf')
        if wt[index] <= W:
            pick = val[index] + self.backtrack(index - 1, W - wt[index], wt, val, dp)
            
        dp[index][W] = max(pick, notPick)
        
        return dp[index][W]
    
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       dp = [[-1] * (W + 1) for _ in range(n)]
       
       return self.backtrack(n - 1, W, wt, val, dp)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends