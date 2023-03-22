#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        # code here
        count = 0
        copy = N

        while copy > 0:
            d = copy % 10
            
            if d != 0 and N % d == 0:
                count += 1

            copy = copy // 10
            
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends