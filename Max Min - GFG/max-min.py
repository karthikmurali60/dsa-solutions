class Solution:
    def findSum(self,A,N): 
        #code here
        
        minEle, maxEle = float('inf'), -float('inf')
        
        for num in A:
            minEle = min(minEle, num)
            maxEle = max(maxEle, num)
            
        return minEle + maxEle



#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    ob = Solution()
    print(ob.findSum(a,n))
# } Driver Code Ends