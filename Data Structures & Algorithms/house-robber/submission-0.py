class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(idx: int) -> int:
            if idx >= len(nums):
                return 0
            if idx in memo:
                return memo[idx]

            memo[idx] = nums[idx] + max(dfs(idx + 2), dfs(idx + 3))
            return memo[idx]

        return max(dfs(0), dfs(1))