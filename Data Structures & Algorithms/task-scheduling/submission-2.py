class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-x for x in counts.values()]
        heapq.heapify(max_heap)

        time = 0
        queue = deque()
        while max_heap or queue:
            time += 1

            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    queue.append([cnt, time + n])
            else:
                time = queue[0][1]

            if queue and time == queue[0][1]:
                heapq.heappush(max_heap, queue.popleft()[0])

        return time

            