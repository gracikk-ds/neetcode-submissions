class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_hash: dict[str, int] = {}
        for digit in s1:  # O(n)
            s1_hash[digit] = s1_hash.get(digit, 0) + 1

        left: int = 0
        perm_hash: dict[str, int] = {}
        for idx in range(len(s2)):  # O(n)
            print("before", perm_hash)
            if idx > len(s1) - 1:
                perm_hash[s2[left]] -= 1
                if perm_hash[s2[left]] == 0:
                    perm_hash.pop(s2[left])
                left += 1

            perm_hash[s2[idx]] = perm_hash.get(s2[idx], 0) + 1
            print("after", perm_hash, s1_hash)
            if perm_hash == s1_hash:  # O(26) == O(1)
                return True

        return False