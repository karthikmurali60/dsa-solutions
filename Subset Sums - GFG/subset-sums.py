#User function Template for python3
class Solution:
    def backtrack(self, index, arr, N, result, ds):
        if index == N:
            result.append(sum(ds))
            return
        
        # pick the element at the current index.
        ds.append(arr[index])
        self.backtrack(index + 1, arr, N, result, ds)
        ds.pop()
        
        # do not pick the element at the current index.
        self.backtrack(index + 1, arr, N, result, ds)
    
	def subsetSums(self, arr, N):
		# code here
		
		result = []
		
		self.backtrack(0, arr, N, result, [])
		
		return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends