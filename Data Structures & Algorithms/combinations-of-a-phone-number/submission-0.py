class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        res = []
        sol = []
        maps = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
        }

        def backtrack(idx: int) -> None:
            if idx == n:
                if sol:
                    res.append("".join(sol[:]))
                return

            for possible_val in maps[digits[idx]]:
                sol.append(possible_val)
                backtrack(idx + 1)
                sol.pop()

        backtrack(0)
        return res
