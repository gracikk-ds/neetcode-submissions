class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagrams always have same number of chars.
        if len(s) != len(t):
            return False
        
        # identical lines are anagrams
        if s == t:
            return True

        hash_map_s: dict[str: int] = {}
        for s_el in s:
            hash_map_s[s_el] = hash_map_s.get(s_el, 0) + 1
        
        hash_map_t: dict[str: int] = {}
        for t_el in t:
            hash_map_t[t_el] = hash_map_t.get(t_el, 0) + 1      

        for key in hash_map_s:
            if hash_map_t.get(key, 0) == hash_map_s.get(key, 0):
                continue
            return False
        return True