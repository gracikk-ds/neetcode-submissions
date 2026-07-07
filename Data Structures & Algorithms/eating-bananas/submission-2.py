class Solution:
    def get_max_val(self, piles: list[int]) -> int:
        """find max value of the sequence."""
        max_value = 0
        for el in piles:
            if el > max_value:
                max_value = el
        return max_value

    def measure_time(self, piles: list[int], eating_rate: int) -> int:
        """measure time needed to eat all bananas with given eating_rate."""
        time_taken = 0
        for pile in piles:
            time_taken += math.ceil(pile / eating_rate)
        return time_taken

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles -> [4, 6, 2, 11, 15]
        # hours: 8
        # eating_rate: ?
        max_bananas = self.get_max_val(piles)

        # we can go through all possible values for eating_rate - [1, max_value]
        best_option = max_bananas
        left = 1
        right = max_bananas
        while left <= right:
            eating_rate = left + (right - left) // 2
            time_taken = self.measure_time(piles, eating_rate)
            if time_taken > h:
                left = eating_rate + 1
            elif time_taken <= h:
                best_option = min(eating_rate, best_option)
                right = eating_rate - 1
        
        return best_option
