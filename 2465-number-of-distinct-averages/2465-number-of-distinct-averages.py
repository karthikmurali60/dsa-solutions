class Solution:
    def findMinimum(self, nums):
        minEle, index = 1e9, -1
        
        for ind, num in enumerate(nums):
            if num < minEle:
                minEle = num
                index = ind
                
        return index, minEle
    
    def findMaximum(self, nums):
        maxEle, index = -1e9, -1
        
        for ind, num in enumerate(nums):
            if num > maxEle:
                maxEle = num
                index = ind
                
        return index, maxEle
    
    def distinctAverages(self, nums: List[int]) -> int:
        hashMap = {}
        
        while len(nums) != 0:
            minIndex, minEle = self.findMinimum(nums)
            nums.pop(minIndex)
            
            maxIndex, maxEle = self.findMaximum(nums)
            nums.pop(maxIndex)
            
            average = (minEle + maxEle) / 2
            
            hashMap[average] = 1 + hashMap.get(average, 0)
            
        return len(hashMap.keys())
            