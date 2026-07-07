class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        reverse_temps = temperatures[::-1]
        results = [0 for _ in temperatures]
        stack = []
        index_stack = []

        for temp_idx, rev_temp in enumerate(reverse_temps):

            while stack and rev_temp >= stack[-1]:
                stack.pop()
                index_stack.pop()
            
            if not stack:
                results[temp_idx] = 0
            else:
                results[temp_idx] = temp_idx-index_stack[-1]

            stack.append(rev_temp)
            index_stack.append(temp_idx)

        return results[::-1]
            
                
            

            
            


