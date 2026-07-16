class Solution:
    def isvalid(self, string: Optional[str]) -> bool:
        # валидны только 1 или 2 цифры, без ведущего нуля, в диапазоне 1..26
        return bool(string) and string[0] != "0" and 1 <= int(string) <= 26

    def numDecodings(self, s: str) -> int:
        length: int = len(s)
        cache = {}

        def count(idx: int) -> int:
            if idx == length:  # дошли до конца — одно валидное разбиение
                return 1

            if idx in cache:
                return cache[idx]

            total = 0
            if self.isvalid(s[idx : idx + 1]):  # берём одну цифру
                total += count(idx + 1)
            if idx + 2 <= length and self.isvalid(s[idx : idx + 2]):  # берём две цифры
                total += count(idx + 2)
            cache[idx] = total

            return total

        return count(0)
