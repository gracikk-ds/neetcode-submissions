class Solution:
    def trap(self, height: List[int]) -> int:
        left: int = 0
        right: int = len(height) - 1

        left_max: int = height[left]
        right_max: int = height[right]

        area: int = 0
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                area += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                area += right_max - height[right]

        return area