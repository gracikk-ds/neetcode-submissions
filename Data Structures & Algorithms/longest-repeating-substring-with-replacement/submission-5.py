class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left: int = 0
        hashmap: dict[str, int] = {}
        max_length: int = 0

        for idx in range(len(s)):
            length = idx - left + 1
            hashmap[s[idx]] = hashmap.get(s[idx], 0) + 1

            # find top freq value in hash_map
            top_val = 0
            for value in hashmap.values():  # time: O(26)
                top_val = max(top_val, value)

            if k < length - top_val:
                hashmap[s[left]] -= 1
                left += 1
                length -= 1
            
            # max_length = max(max_length, length)
        return length
