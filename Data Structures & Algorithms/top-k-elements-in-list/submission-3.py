class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map: dict[int , int] = defaultdict(int)
        for num in nums:
            hash_map[num] += 1

        freqs = [[] for _ in range(len(nums) + 1)]
        for key, value in hash_map.items():
            freqs[value].append(key)

        result = []
        for freq in freqs[::-1]:
            for num in freq:
                result.append(num)
            if len(result) == k:
                return result


        
