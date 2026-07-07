class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        reverse_temps = temperatures[::-1]
        results = [0 for _ in temperatures]
        stack = []  # pair: [temp, index]

        for temp_idx, rev_temp in enumerate(reverse_temps):

            while stack and rev_temp >= stack[-1][0]:
                stack.pop()
            
            if not stack:
                results[temp_idx] = 0
            else:
                results[temp_idx] = temp_idx - stack[-1][1]

            stack.append([rev_temp, temp_idx])

        return results[::-1]
            
                
            

            
            


