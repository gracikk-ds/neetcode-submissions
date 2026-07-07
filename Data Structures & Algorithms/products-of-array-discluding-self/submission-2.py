class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # Forward pass: output[i] = product of all elements to the LEFT of i
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        # Backward pass: multiply in product of all elements to the RIGHT of i
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output