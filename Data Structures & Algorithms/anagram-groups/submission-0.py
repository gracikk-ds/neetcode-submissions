class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: Dict[tuple, List[str]] = {}

        for string in strs:
            # Build character frequency map
            hash_map: Dict[str, int] = {}
            for symbol in string:
                hash_map[symbol] = hash_map.get(symbol, 0) + 1

            # Convert to a hashable key (sorted for consistency)
            key = tuple(sorted(hash_map.items()))

            groups[key] = groups.get(key, []) + [string]
        return list(groups.values())