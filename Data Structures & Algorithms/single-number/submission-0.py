class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0  # because n ^ 0 = n

        for num in nums:
            res = res ^ num
        return res