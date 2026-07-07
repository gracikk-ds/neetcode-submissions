class Solution:
    def binary_search(self, nums: List[int], target: int) -> int:
        """bin search return INDEX."""
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        return -1

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        if nums[left] <= nums[right]:
            self.binary_search(nums, target)

        while left <= right:
            rotation_point = left + (right - left) // 2

            if nums[rotation_point] > nums[left]:
                left = rotation_point
            elif nums[rotation_point] < nums[left]:
                right = rotation_point
            else:
                break
        rotation_point = left + (right - left) // 2

        index = self.binary_search(nums[rotation_point + 1:], target)
        if index != -1:
            return index + rotation_point + 1

        index = self.binary_search(nums[:rotation_point + 1], target)
        if index != -1:
            return index

        return -1









