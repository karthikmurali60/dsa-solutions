class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxArray, result = [], []
        i, j, n = 0, 0, len(nums)
        
        while j < n:
            if len(maxArray) > 0 and nums[j] > maxArray[-1]:
                while len(maxArray) > 0 and nums[j] > maxArray[-1]:
                    maxArray.pop(-1)
            
            maxArray.append(nums[j])
                
            if j - i + 1 < k:
                j += 1
            else:
                result.append(maxArray[0])
                
                if nums[i] == maxArray[0]:
                    maxArray.pop(0)
                    
                i += 1
                j += 1
                
        return result
        
        
        
        