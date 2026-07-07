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
            # freq = [1, 2]
            # k = 2
            if not freq:
                continue
            freq = freq[:k]
            k -= len(freq)
            result.extend(freq)
            if k == 0:
                return result
        return result


        
