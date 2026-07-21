class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack: list[tuple[int, int]] = []

        max_area: int = 0
        for idx, height in enumerate(heights):
            if not stack:
                stack.append((idx, height))
                max_area = max(max_area, height)
                continue

            old_idx = idx
            while stack and stack[-1][-1] >= height:
                old_idx, old_height = stack.pop()
                area = (idx - old_idx) * old_height
                max_area = max(max_area, area)
            stack.append((old_idx, height))

        max_length: int = len(heights)
        while stack:
            idx, height = stack.pop()
            width = max_length - idx
            area = width * height
            max_area = max(max_area, area)

        return max_area




