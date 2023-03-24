class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        # code here
        
        countMap = {}
        
        for num in arr:
            countMap[num] = 1 + countMap.get(num, 0)
            
        for i in range(1, N + 1):
            if i in countMap:
                arr[i - 1] = countMap[i]
            else:
                arr[i - 1] = 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__=="__main__":
	T=int(input())
	while(T>0):
		N=int(input())
		arr=[int(x) for x in input().strip().split()]
		P=int(input())
		ob=Solution()
		ob.frequencyCount(arr, N, P)
		for i in arr:
			print(i, end=" ")
		print()
		T-=1



# } Driver Code Ends