class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        answer = -1
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                high = mid - 1
            else:
                answer = mid
                low = mid + 1

        return answer + 1