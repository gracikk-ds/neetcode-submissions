class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # create array of points and distances.
        minHeap = []
        for coords in points:
            distance = math.sqrt(coords[0]**2 + coords[1]**2)
            minHeap.append([distance, coords[0], coords[1]])

        # heapify the array
        heapq.heapify(minHeap)

        closest: List[List[int]] = []
        while k > 0:
            dist, x0, x1 = heapq.heappop(minHeap)
            closest.append([x0, x1])
            k -= 1
        return closest