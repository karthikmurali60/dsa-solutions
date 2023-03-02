#User function Template for python3

class Solution:
    def backtrack(self, index, n, price, dp):
        if index == 0:
            return n * price[0]
            
        if dp[index][n] != -1:
            return dp[index][n]
            
        notPick = 0 + self.backtrack(index - 1, n, price, dp)
        
        pick = -1e9
        if index + 1 <= n:
            pick = price[index] + self.backtrack(index, n - (index + 1), price, dp)
            
        dp[index][n] = max(pick, notPick)
        
        return dp[index][n]
    
    def cutRod(self, price, n):
        dp = [[-1] * (n + 1) for _ in range(len(price))]
        
        return self.backtrack(len(price) - 1, n, price, dp)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends