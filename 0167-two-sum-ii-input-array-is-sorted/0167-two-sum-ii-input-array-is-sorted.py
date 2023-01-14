class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            currSum = numbers[left] + numbers[right]
            
            if target == currSum:
                return [left + 1, right + 1]
            
            if target > currSum:
                left += 1
            else:
                right -= 1