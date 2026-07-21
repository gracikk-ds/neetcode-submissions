class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result: list[int] = [0 for _ in range(len(temperatures))]
        stack: list[tuple(int, int)] = []
        for cur_idx, cur_temp in enumerate(temperatures):
            if not stack:
                stack.append((cur_idx, cur_temp))
                continue
            
            while stack and stack[-1][-1] < cur_temp:
                idx, temp = stack.pop()
                result[idx] = cur_idx - idx
            stack.append((cur_idx, cur_temp))
        return result