class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: dict[tuple, List[str]] = defaultdict(list)

        for string in strs:
            # Build character frequency map
            hash_map: dict[str, int] = defaultdict(int)
            for symbol in string:
                hash_map[symbol] += 1

            # Convert to a hashable key (sorted for consistency)
            key = tuple(sorted(hash_map.items()))

            groups[key].append(string)
        return list(groups.values())