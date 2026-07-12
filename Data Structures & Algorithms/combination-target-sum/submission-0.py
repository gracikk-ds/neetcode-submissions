class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtrack(idx: int, remaining: int) -> None:
            if remaining == 0:
                res.append(sol.copy())
                return

            if remaining < 0:
                return

            # pick any number
            for idx in range(idx, n):
                sol.append(nums[idx])
                backtrack(idx, remaining - nums[idx])
                sol.pop()

        backtrack(0, target)
        return res
