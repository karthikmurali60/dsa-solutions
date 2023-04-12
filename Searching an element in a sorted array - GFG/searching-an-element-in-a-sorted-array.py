#User function Template for python3

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, K):
        #Your code here
        low, high = 0, N - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] == K:
                return 1
            
            if arr[mid] > K:
                high = mid - 1
            else:
                low = mid + 1
                
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
	t = int(input())
	for _ in range(t):
		NK = input().strip().split()
		N = int(NK[0])
		K = int(NK[1])
		A = [ int(x) for x in input().strip().split() ]
		ob=Solution()
		print(ob.searchInSorted(A,N,K))

# } Driver Code Ends