class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        base_hm = {}
        for el in s1:  # linear time
            base_hm[el] = base_hm.get(el, 0) + 1

        window_length: int = len(s1)  # const time
        left_pointer: int = 0
        inner_hm = {}
        for idx, symb in enumerate(s2):  # linear * linear -> n^2
            current_length = idx - left_pointer + 1
            inner_hm[symb] = inner_hm.get(symb, 0) + 1
            if current_length < window_length: 
                continue
            
            # compare to hash_maps
            print(inner_hm)
            if inner_hm == base_hm:  # linear 
                return True
            inner_hm[s2[left_pointer]] -= 1
            if inner_hm[s2[left_pointer]] == 0:
                inner_hm.pop(s2[left_pointer])
            left_pointer += 1
        return False


            
            
        