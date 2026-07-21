class Solution:
    def trap(self, height: List[int]) -> int:
        max_left: list[int] = []
        max_right: list[int] = []
        
        # find max except self from the left
        pointer: int = 0
        for element in height:
            max_left.append(pointer)
            pointer = max(pointer, element)
        
        # find max except self from the right
        pointer: int = 0
        for element in height[::-1]:
            max_right.append(pointer)
            pointer = max(pointer, element)
        max_right = max_right[::-1]

        # compute area of the water
        area: int = 0
        for element, left, right in zip(height, max_left, max_right):
            current_area = max(min(left, right) - element, 0)
            area += current_area
        
        return area