class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        sol = []

        def backtrack(idx):
            if idx == n:
                res.append(sol.copy())
                return

            # Don't pick nums at idx
            backtrack(idx + 1)

            # Pick nums at idx
            sol.append(nums[idx])
            backtrack(idx + 1)
            sol.pop()

        backtrack(0)
        return res
