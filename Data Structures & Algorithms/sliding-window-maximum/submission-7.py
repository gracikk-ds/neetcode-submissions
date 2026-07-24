class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque([])
        max_storage = []

        for idx in range(len(nums)):
            # add new element to the queue
            while queue and nums[queue[-1]] <= nums[idx]:
                queue.pop()  # pop from the right as a stack.
            queue.append(idx)

            # if the queue is to large, pop old elements from the left
            if queue[0] <= idx - k:
                queue.popleft()

            if idx >= k - 1:
                max_storage.append(nums[queue[0]])
        return max_storage

