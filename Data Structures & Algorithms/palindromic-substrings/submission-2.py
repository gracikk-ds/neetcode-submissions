class Solution:

    def count_pals(self, s: str, i: int, j: int) -> int:
        num_pals = 0
        while i >= 0 and j < len(s) and s[i] == s[j]:
            num_pals += 1
            i -= 1
            j += 1
        return  num_pals

    def countSubstrings(self, s: str) -> int:
        num_pals: int = 0

        for idx in range(len(s)):
            # odd case
            num_pals += self.count_pals(s, idx, idx)

            # even case
            num_pals += self.count_pals(s, idx, idx + 1)

        return num_pals
        