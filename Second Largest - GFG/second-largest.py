#User function Template for python3
class Solution:

	def print2largest(self,arr, n):
		# code here
		
		largest, ans = -1e9, -1e9
		
		for num in arr:
		    largest = max(largest, num)
		    
		for num in arr:
		    if num > ans and num != largest:
		        ans = num
		        
		return ans if ans != -1e9 else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends