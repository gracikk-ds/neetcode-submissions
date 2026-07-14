class Solution:

    def is_palindrom(self, string: str) -> bool:
        left, right = 0, len(string) - 1

        while left <= right:
            if string[left] == string[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

    def partition(self, s: str) -> List[List[str]]:

        res, sol = [], []

        def backtrack(substring: str) -> None:
            if not substring:
                if sol:
                    res.append(sol[:])
                return 

            for idx in range(1, len(substring) + 1):
                left, right = substring[:idx], substring[idx:]
                if self.is_palindrom(left):
                    sol.append(left)
                    backtrack(right)
                    sol.pop()
                else:
                    continue

        backtrack(s)
        return res
        

        