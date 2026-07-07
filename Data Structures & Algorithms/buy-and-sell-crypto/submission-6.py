class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_pointer: int = 0
        right_pointer: int = 0

        max_reward: int = 0
        while right_pointer < len(prices) - 1:
            right_pointer += 1
            reward = prices[right_pointer] - prices[left_pointer]
            max_reward = max(max_reward, reward)

            if prices[right_pointer] < prices[left_pointer]:
                left_pointer = right_pointer

        return max_reward