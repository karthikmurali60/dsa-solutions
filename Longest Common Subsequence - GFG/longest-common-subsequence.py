#User function Template for python3

class Solution:
    def backtrack(self, index1, index2, s1, s2, dp):
        if index1 < 0 or index2 < 0:
            return 0
            
        if dp[index1][index2] != -1:
            return dp[index1][index2]
            
        if s1[index1] == s2[index2]:
            dp[index1][index2] = 1 + self.backtrack(index1 - 1, index2 - 1, s1, s2, dp)
            return dp[index1][index2]
            
        dp[index1][index2] = max(self.backtrack(index1 - 1, index2, s1, s2, dp), self.backtrack(index1, index2 - 1, s1, s2, dp))
        return dp[index1][index2]
    
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        dp = [[-1] * (y + 1) for _ in range(x + 1)]
        
        return self.backtrack(x - 1, y - 1, s1, s2, dp)
        

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
        x,y = map(int,input().strip().split())
        s1 = str(input())
        s2 = str(input())
        ob=Solution()
        print(ob.lcs(x,y,s1,s2))
# } Driver Code Ends