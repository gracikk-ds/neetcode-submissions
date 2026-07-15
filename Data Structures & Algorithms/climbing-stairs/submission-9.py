class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(score: int):
            if score in memo:
                return memo[score]
            if score > n:
                return 0
            if score == n:
                return 1
            num_ways_to_reach = dfs(score + 1) + dfs(score + 2)
            memo[score] = num_ways_to_reach
            return num_ways_to_reach
        
        dfs(0)
        return memo[0]
