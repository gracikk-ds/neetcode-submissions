class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars_info = [(pos, sp) for pos, sp in zip(position, speed)]
        cars_info.sort(reverse=True)

        fleets = []
        for pos, sp in cars_info:
            time_to_arr = (target - pos) / sp
            fleets.append(time_to_arr)
            if len(fleets) >= 2 and fleets[-1] <= fleets[-2]:
                fleets.pop()

        return len(fleets)