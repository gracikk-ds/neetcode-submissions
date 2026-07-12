class Solution:
    def climbStairs(self, n: int) -> int:
        memo: dict[int, int] = {}

        def count_ways(steps: int) -> int:
            if steps > n:
                return 0
            if steps == n:
                return 1
            if steps in memo:
                return memo[steps]

            memo[steps] = count_ways(steps + 1) + count_ways(steps + 2)
            return memo[steps]

        return count_ways(0)
