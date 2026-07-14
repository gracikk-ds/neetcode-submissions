class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sum(range(0, n + 1)) - sum(nums)
        n = len(nums)  # начинаем с n — это последнее число диапазона

        for i in range(len(nums)):
            n += i  # sum(range(0, n + 1))
            n -= nums[i]  # - sum(nums)
        return n