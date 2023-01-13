class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        left, right = 0, len(nums) - 1
        
        while left <= right:
            # In this case, the array is not rotated or rotated n times.
            # Basically even after rotation, the resulting array is the
            # same as the original array which is sorted and the min value
            # is present at the left position.
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break
                
            mid = int((left + (right - left) / 2))
            result = min(result, nums[mid])
            
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
                
        return result
        