class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # sorting: nlogn -> n + klogn
        nums = [-x for x in nums]
        heapq.heapify(nums)  # O(n)

        kth_largest = None
        while k > 0:
            kth_largest = -heapq.heappop(nums)
            k -= 1
        return kth_largest