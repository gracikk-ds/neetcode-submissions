class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_elements: list[int] = []

        for idx in range(len(nums)):
            current_window: list[int]  = []
            if idx + k - 1 < len(nums):
                for w_idx in range(k):
                    current_window.append(nums[idx + w_idx])
                w_max: int = max(current_window)
                max_elements.append(w_max)

        return max_elements

