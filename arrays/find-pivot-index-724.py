from turtle import left


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        arraySum = sum(nums)
        leftSum = 0

        for i, num in enumerate(nums):
            if leftSum == (arraySum - num - leftSum):
                return i

            leftSum += num

        return -1
