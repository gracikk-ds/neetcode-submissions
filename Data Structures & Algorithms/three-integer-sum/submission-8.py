class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        nums.sort()

        triplets: list[list[int]] = []
        for idx in range(len(nums)):
            if nums[idx] > 0:
                return triplets

            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue

            left: int = idx + 1
            right: int = len(nums) - 1
            while left < right:
                total = nums[idx] + nums[left] + nums[right]
                if total == 0:
                    triplets.append([nums[idx], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while (left < right
                        and nums[left] == nums[left - 1]
                        and nums[right] == nums[right + 1]
                    ):
                        left += 1
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return triplets
