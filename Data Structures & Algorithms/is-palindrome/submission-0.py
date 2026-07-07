class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([x.lower() for x in s if x.isalnum()])

        i: int = 0
        j: int = len(s) - 1
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
                continue
            else:
                return False
        return True