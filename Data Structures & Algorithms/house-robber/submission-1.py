class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(idx: int) -> int:
            if idx >= len(nums):
                return 0
            if idx in memo:
                return memo[idx]

            # max(robbe or skip)
            memo[idx] = max(dfs(idx + 1), nums[idx] + dfs(idx + 2))
            return memo[idx]

        return max(dfs(0), dfs(1))