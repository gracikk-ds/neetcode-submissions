class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = None

        for idx in range(len(nums)):
            curr_prod = nums[idx]
            max_prod = curr_prod if max_prod is None else max(max_prod, curr_prod)
            for j in range(idx + 1, len(nums)):
                curr_prod *= nums[j]
                max_prod = max(max_prod, curr_prod)

        return max_prod
