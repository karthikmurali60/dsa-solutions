#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        i, j = 0, 0
        cs, ms = 0, -float('inf')
        
        while j < N:
            cs += Arr[j]

            if j - i + 1 < K:
                j += 1
            else:
                ms = max(ms, cs)
                cs -= Arr[i]
                i += 1
                j += 1
                
        return ms
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends