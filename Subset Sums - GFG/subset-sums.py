#User function Template for python3
class Solution:
    def dfs(self, index, arr, ds, ans):
        if index == len(arr):
            ans.append(list(ds))
            return
        
        # pick
        ds.append(arr[index])
        self.dfs(index + 1, arr, ds, ans)
        ds.pop()
        
        # not pick
        self.dfs(index + 1, arr, ds, ans)
    
	def subsetSums(self, arr, N):
		# code here
		ans = []
		result = []
		
		self.dfs(0, arr, [], ans)
		
		for subset in ans:
		    result.append(sum(subset))
		    
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