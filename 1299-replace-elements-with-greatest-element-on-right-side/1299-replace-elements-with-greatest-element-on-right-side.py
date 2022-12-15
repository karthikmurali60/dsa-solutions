class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = [-1] * len(arr)
        currMax = -1
        
        for i in range(len(arr) - 1, 0, -1):
            currMax = max(currMax, arr[i])
            result[i - 1] = currMax
            
        return result