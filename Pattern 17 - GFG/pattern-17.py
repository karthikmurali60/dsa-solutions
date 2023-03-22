#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(1, N + 1):
            for j in range(N - i):
                print(" ", end="")
            
            for j in range(65, 65 + i):
                print(chr(j), end="")
            
            for k in range(65 + i - 1, 65, -1):
                print(chr(k - 1), end="")
            
            print()

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends