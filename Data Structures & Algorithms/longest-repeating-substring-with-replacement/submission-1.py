class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left: int = 0

        hash_map: dict[str, int] = {}  # space: O(26)
        max_length: int = 0
        for right, symb in enumerate(s, start=1):  # time: O(n)
            hash_map[symb] = hash_map.get(symb, 0) + 1
            length = right - left

            # find top freq value in hash_map
            top_val = 0
            for value in hash_map.values():  # time: O(26)
                top_val = max(top_val, value)

            if length - top_val <= k:
                max_length = max(max_length, length)
            else:
                hash_map[s[left]] -= 1
                left += 1
        return max_length



