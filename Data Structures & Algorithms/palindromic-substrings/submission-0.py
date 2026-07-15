class Solution:
    def countSubstrings(self, s: str) -> int:
        num_pals: int = 0

        for idx in range(len(s)):

            # odd case
            i, j = idx, idx
            while i >= 0 and j < len(s) and s[i] == s[j]:
                num_pals += 1
                i -= 1
                j += 1

            # even case
            i, j = idx, idx + 1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                num_pals += 1
                i -= 1
                j += 1

        return num_pals
        