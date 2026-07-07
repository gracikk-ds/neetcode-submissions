class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map: dict[str, list[int, ...]] = {}
        for idx, num in enumerate(nums):
            hash_map[num] = idx

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in hash_map and hash_map[diff] != idx:
                return [idx, hash_map[diff]]
        return []


                    
