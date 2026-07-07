class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_pointer: int = 0
        right_pointer: int = len(heights) - 1

        max_area = 0
        while left_pointer < right_pointer:
            length = right_pointer - left_pointer
            min_wall = min(heights[left_pointer], heights[right_pointer])
            current_area = length * min_wall
            if max_area < current_area:
                max_area = current_area

            if heights[right_pointer] > heights[left_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
        return max_area
            
