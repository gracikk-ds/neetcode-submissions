class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashset = set()

        for num in nums:
            if num in hashset:
                return num
            hashset.add(num)