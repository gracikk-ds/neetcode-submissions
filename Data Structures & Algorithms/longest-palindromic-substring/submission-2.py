class Solution:

    def palindrome(self, string: str) -> bool:
        left, right = 0, len(string) - 1

        while left <= right:
            if string[left] == string[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j + 1]
                if len(sub) > len(res) and self.palindrome(sub):
                    res = sub

        return res

