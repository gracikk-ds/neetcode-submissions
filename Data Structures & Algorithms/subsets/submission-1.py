class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        res, sol = [], []

        def bactrack(idx: int) -> None:
            if idx == n:
                res.append(sol.copy())
                return 

            # do not pick the number
            bactrack(idx + 1)

            # pick the number
            sol.append(nums[idx])
            bactrack(idx + 1)
            sol.pop()

        bactrack(0)
        return res