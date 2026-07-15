class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_length = len(res)
        
        
        for idx in range(len(s)):
            i, j = idx, idx
            while i >= 0 and j < len(s) and s[i] == s[j]:
                length = j - i + 1
                if length > res_length:
                    res = s[i: j + 1]
                    res_length = length
                j += 1
                i -= 1

            i, j = idx, idx + 1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                length = j - i + 1
                if length > res_length:
                    res = s[i: j + 1]
                    res_length = length
                j += 1
                i -= 1

        return res

