class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtrack(idx: int, vals: list[int]) -> None:
            if idx >= n:
                res.append(sol[:])
                return

            if not vals:
                return

            for i, val in enumerate(vals):
                sol.append(val)
                # send vals with no val in it.
                new_vals = vals[:i] + vals[i + 1 :]
                backtrack(idx + 1, new_vals)
                sol.pop()

            return

        backtrack(0, nums.copy())
        return res
