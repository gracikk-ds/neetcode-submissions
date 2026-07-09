class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first_heaviest = -heapq.heappop(stones)
            second_heaviest = -heapq.heappop(stones)

            if first_heaviest == second_heaviest:
                continue
            
            residual = first_heaviest - second_heaviest
            heapq.heappush(stones, -residual)
        return -stones[0] if stones else 0