class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dfs(idx: int) -> int:
            if idx >= len(cost):
                return 0

            if idx in memo:
                return memo[idx]
            memo[idx] = cost[idx] + min(dfs(idx + 1), dfs(idx + 2))
            return memo[idx]

        return min(dfs(0), dfs(1))