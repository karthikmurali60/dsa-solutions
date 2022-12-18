class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        result = []
        i, j = 0, 0
        tempList = []
        
        while j < len(nums):
            while len(tempList) > 0 and nums[j] > tempList[-1]:
                tempList.pop()
                
            tempList.append(nums[j])
                
            if j - i + 1 < k:
                j += 1
            else:
                result.append(tempList[0])
                
                if tempList[0] == nums[i]:
                    tempList.pop(0)
                    
                i += 1
                j += 1
                
        return result
