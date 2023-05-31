
class Solution:
    def trappingWater(self, arr,n):
        #Code here
        left, right = 0, n - 1
        leftMax, rightMax = 0, 0
        result = 0
        
        while left <= right:
            if arr[left] <= arr[right]:
                if arr[left] > leftMax:
                    leftMax = arr[left]
                else:
                    result += leftMax - arr[left]
                   
                left += 1 
            else:
                if arr[right] > rightMax:
                    rightMax = arr[right]
                else:
                    result += rightMax - arr[right]
                
                right -=1
        
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends