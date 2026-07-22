class Solution:
    def minWindow(self, s: str, t: str) -> str:
        thash: dict[str, int] = {}
        for char in t:
            thash[char] = thash.get(char, 0) + 1
        needed_matches: int = len(thash)

        # s = OBYYXBZOBXYZB: YXBZ, XYZ
        # OBYYXBZ -> YXBZ -> XBZ
        # XBZ -> XBZOBXY -> ZOBXY -> OBXY
        # OBXYZ -> XYZ -> YZ -> YZB
        current_hash: dict[str, int] = {}
        substring: str = ""
        left: int = 0
        we_get_matches: int = 0

        for idx in range(len(s)):
            current_hash[s[idx]] = current_hash.get(s[idx], 0) + 1

            if s[idx] in thash and current_hash[s[idx]] == thash[s[idx]]:
                we_get_matches += 1
            # print(we_get_matches, needed_matches, we_get_matches == needed_matches)

            while we_get_matches == needed_matches:
                if substring == "" or len(s[left: idx + 1]) < len(substring):
                    substring = s[left: idx + 1]
                # print(substring)
                current_hash[s[left]] -= 1
                if s[left] in thash and current_hash[s[left]] < thash[s[left]]:
                    we_get_matches -= 1
                left += 1
        return substring




            

