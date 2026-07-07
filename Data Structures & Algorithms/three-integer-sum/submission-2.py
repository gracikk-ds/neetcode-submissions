class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # nlogn

        outputs: list[list[int]] = []
        for idx, num in enumerate(nums):
            if num > 0:
                break

            if idx > 0 and num == nums[idx-1]:
                continue

            left: int = idx + 1
            right: int = len(nums) - 1
            while left < right:
                target = nums[left] + nums[right] + num
                if target == 0:
                    outputs.append([nums[idx], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                
                if target > 0:
                    right -= 1
                    continue

                if target < 0:
                    left += 1
        return outputs