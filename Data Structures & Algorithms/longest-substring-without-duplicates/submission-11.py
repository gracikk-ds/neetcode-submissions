class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map: dict[str, int] = {}
        left: int = 0
        max_length: int = 0

        for idx in range(len(s)):
            if s[idx] in hash_map:
                left = max(hash_map[s[idx]] + 1, left)
            
            max_length = max(max_length, idx - left + 1)
            hash_map[s[idx]] = idx
        
        return max_length
            





