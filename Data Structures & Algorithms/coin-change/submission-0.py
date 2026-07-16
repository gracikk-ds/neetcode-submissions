class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins: Optional[int] = None
        cache = {}

        def dfs(left) -> None:
            if left == 0:
                return 0
            
            if left < 0:
                return 

            if left in cache:
                return cache[left]

            nums_ways = []
            for coin in coins:
                res = dfs(left - coin)
                if res is not None:
                    nums_ways.append(res + 1)  # +1 за текущую монету

            cache[left] = min(nums_ways) if nums_ways else None
            return cache[left]

        result = dfs(amount)
        return result if result is not None else -1