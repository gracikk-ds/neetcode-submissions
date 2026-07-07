class TimeMap:

    def __init__(self):
        self.cache: dict[str, list[list[int, str]]] = {}

    def binary_search(self, vals: list[int, str], target: int) -> int:
        left = 0
        right = len(vals) - 1
        value = ""

        while left <= right:
            middle = left + (right - left) // 2
            if vals[middle][0] > target:
                right = middle - 1
            elif vals[middle][0] <= target:
                left = middle + 1
                value = vals[middle][1]
        return value

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cache:
            self.cache[key] = []
        self.cache[key].append([timestamp, value])
        # self.cache[key].sort(key=lambda x:x[0])
        
    def get(self, key: str, timestamp: int) -> str:
        entries = self.cache.get(key, [])
        return self.binary_search(entries, timestamp)

