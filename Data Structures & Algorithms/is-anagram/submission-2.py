class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagrams always have same number of chars.
        if len(s) != len(t):
            return False

        countS: dict[str: int] = {}
        countT: dict[str, int] = {}
        
        for idx in range(len(s)):
            countS[s[idx]] = countS.get(s[idx], 0) + 1
            countT[t[idx]] = countT.get(t[idx], 0) + 1
        return countS == countT