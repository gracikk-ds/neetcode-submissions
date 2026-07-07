class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_pointer: int = 0
        right_pointer: int = 0

        max_length: int = 0
        while right_pointer <= len(s):
            sub_str = s[left_pointer: right_pointer]

            hash_map: dict[str, int] = {}
            is_unique = True
            for el in sub_str:
                if el in hash_map:
                    left_pointer += 1
                    break
                hash_map[el] = 1
            if is_unique:
                max_length = max(max_length, right_pointer - left_pointer)
            right_pointer += 1
        return max_length