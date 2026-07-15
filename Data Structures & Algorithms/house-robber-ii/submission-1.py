class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        memo = {}

        def dfs(idx, is_last_check: bool) -> int:
            limit = n - 1 if is_last_check else n
            if idx >= limit:
                return 0

            key = (idx, is_last_check)
            if key in memo:
                return memo[key]

            memo[key] = nums[idx] + max(dfs(idx + 2, is_last_check), dfs(idx + 3, is_last_check))       
            return memo[key]

        return max(dfs(0, True), dfs(1, False), dfs(2, False))