class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # for each car we compute time needed for a car to reach the finish line
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        
        stack = []
        for car in cars:
            pos, speed = car
            time_to_ar = (target - pos) / speed
            stack.append(time_to_ar)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
        