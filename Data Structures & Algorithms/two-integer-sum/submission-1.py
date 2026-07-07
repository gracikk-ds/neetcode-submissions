class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx_first, el_first in enumerate(nums):
            for idx_second, el_second in enumerate(nums):
                if idx_second > idx_first and el_first + el_second == target:
                    return [idx_first, idx_second]

                    
