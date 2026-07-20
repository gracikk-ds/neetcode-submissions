class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)

        longest_seq = 0
        for num in hash_set:
            if num - 1 not in hash_set:
                length = 1
                while num + length in hash_set:
                    length += 1

                longest_seq = max(longest_seq, length)
        return longest_seq