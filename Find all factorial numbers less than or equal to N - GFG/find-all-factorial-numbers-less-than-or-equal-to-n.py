#User function Template for python3

class Solution:
    def factorialNumbers(self, N):
    	#code here
    	
    	i = 1
    	prod = 1
    	ans = []
    	
    	while prod <= N:
    	    ans.append(prod)
    	    
    	    i += 1
    	    
    	    prod *= i
    	    
    	return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()
        
# } Driver Code Ends