class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_pointer: int = 0
        storage = {}

        max_length: int = 0
        for idx, value in enumerate(s):
            if value in storage:
                left_pointer = max(storage[value] + 1, left_pointer)
            storage[value] = idx
            max_length = max(idx - left_pointer + 1, max_length)

        return max_length