class Solution:
    def reverse(self, arr, start, end):
        while start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        
    def leftRotate(self, arr, k, n):
        # Your code goes here
        
        if k == 0:
            return
        
        k = k % n
        
        self.reverse(arr, 0, k - 1)
        self.reverse(arr, k, n - 1)
        
        self.reverse(arr, 0, n - 1)


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        k=l[1]
        a = list(map(int,input().split()))
        ob = Solution()
        ob.leftRotate(a,k,n)
        print(*a)
# } Driver Code Ends