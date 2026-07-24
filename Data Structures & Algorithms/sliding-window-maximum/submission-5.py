class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap: list[int] = []
        max_storage: list[int] = []

        for idx, n in enumerate(nums):
            heapq.heappush(heap, (-n, idx))

            while heap[0][1] <= idx - k:
                heapq.heappop(heap)

            if idx >= k - 1:
                max_storage.append(-heap[0][0])
        return max_storage
