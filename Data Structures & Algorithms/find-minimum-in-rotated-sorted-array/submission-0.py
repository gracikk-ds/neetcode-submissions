class Solution:

    def findMin(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums) - 1

        if nums[left] <= nums[right]:
            return nums[left]

        while left <= right:
            middle = left + (right - left) // 2

            if nums[middle] > nums[left]:
                left = middle
            elif nums[middle] < nums[left]:
                right = middle
            else:
                break

        rotation_point = left + (right - left) // 2
        return nums[rotation_point + 1]
