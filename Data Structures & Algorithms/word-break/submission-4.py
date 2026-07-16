class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordDict = set(wordDict)
        cache = {}

        def backtrack(left: int, right: int):
            if (left, right) in cache:
                return cache[(left, right)]

            if right > n:
                if right - 1 == left:
                    return True
                return False

            if s[left:right] in wordDict:
                cache[(left, right)] = backtrack(right, right + 1) or backtrack(left, right + 1)
                return cache[(left, right)]
            cache[(left, right)] = backtrack(left, right + 1)
            return cache[(left, right)]

        return backtrack(0, 1)
