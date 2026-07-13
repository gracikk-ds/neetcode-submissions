class Solution:
    def check_if_valid(self, string: list[str]) -> bool:
        stack = []

        for par in string:
            if par == "(":
                stack.append(par)
            else:
                if not stack:
                    return False
                stack.pop()
        if not stack:
            return True
        return False

    def generateParenthesis(self, n: int) -> List[str]:
        res, sol = [], []
        num_pars = n * 2

        def backtrack(idx: int) -> None:
            if idx == num_pars:
                if self.check_if_valid(sol):
                    res.append("".join(sol))
                return

            sol.append("(")
            backtrack(idx + 1)
            sol.pop()

            sol.append(")")
            backtrack(idx + 1)
            sol.pop()

        backtrack(0)
        return res
