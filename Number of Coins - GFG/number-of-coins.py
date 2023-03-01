#User function Template for python3
class Solution:
    def backtrack(self, index, V, coins, dp):
        if index == 0:
            if V % coins[index] == 0:
                return int(V / coins[index])
                
            return float('inf')
            
        if dp[index][V] != -1:
            return dp[index][V]
            
        notPick = 0 + self.backtrack(index - 1, V, coins, dp)
        
        pick = float('inf')
        if coins[index] <= V:
            pick = 1 + self.backtrack(index, V - coins[index], coins, dp)
            
        dp[index][V] = min(pick, notPick)
        
        return dp[index][V]
    
	def minCoins(self, coins, M, V):
		# code here
		
		dp = [[-1] * (V + 1) for _ in range(M)]
		
		ans = self.backtrack(M - 1, V, coins, dp)
		
		return ans if ans != float('inf') else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		v,m = input().split()
		v,m = int(v), int(m)
		coins = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minCoins(coins,m,v)
		print(ans)

# } Driver Code Ends