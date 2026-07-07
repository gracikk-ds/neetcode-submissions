class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map: dict[int , int] = defaultdict(int)
        for num in nums:
            hash_map[num] += 1

        hash_map = {key: value for key, value in sorted(hash_map.items(), key=lambda x: x[1], reverse=True)}
        return [key for idx, (key, _) in enumerate(hash_map.items()) if idx < k]