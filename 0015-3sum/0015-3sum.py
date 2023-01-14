class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        nums.sort()
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left, right = i + 1, len(nums) - 1
                        
            while left < right:
                currSum = nums[left] + nums[right]
                
                if currSum == -nums[i]:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    
                elif currSum > -nums[i]:
                    right -= 1
                else:
                    left += 1
         
        return result
            
                