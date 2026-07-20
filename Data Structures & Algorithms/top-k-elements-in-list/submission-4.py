class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap: dict[int, int] = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        freq_bucket: list[list[int]] = [[] for _ in nums]
        for num, times in hashmap.items():
            freq_bucket[times - 1].append(num)
        freq_bucket = freq_bucket[::-1]

        # pop k most frequent elements
        top_freq_elements = []
        for bucket in freq_bucket:
            while bucket and k > 0:
                top_freq_elements.append(bucket.pop())
                k -= 1
        return top_freq_elements
        