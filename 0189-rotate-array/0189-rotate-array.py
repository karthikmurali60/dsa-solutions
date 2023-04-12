class Solution:
    def reverse(self, nums, start, end):
        while start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
            
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        k = k % n
        
        # reverse the first k elements
        self.reverse(nums, 0, n - k - 1)
        
        # reverse the remaining elements
        self.reverse(nums, n - k, n - 1)
        
        # reverse the entire array, resulting in k rotations
        self.reverse(nums, 0, n - 1)
