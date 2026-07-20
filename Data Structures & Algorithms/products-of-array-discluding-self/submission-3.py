class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for _ in nums]

        prefix: int = 1
        for idx in range(len(nums)):
            output[idx] *= prefix
            prefix *= nums[idx]

        suffix: int = 1
        for idx in range(-1, -len(nums) - 1, -1):
            output[idx] *= suffix
            suffix *= nums[idx]

        return output