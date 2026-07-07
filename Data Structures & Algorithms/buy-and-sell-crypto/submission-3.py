class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ranges_array: list[int] = list(range(0, len(prices) - 1))
        print(ranges_array)

        max_reward: int = 0
        for possible_range in ranges_array:
            possible_range += 1
            start_point: int = 0
            while start_point + possible_range < len(prices):
                max_reward = max(prices[start_point + possible_range] - prices[start_point], max_reward)
                start_point += 1
        return max_reward