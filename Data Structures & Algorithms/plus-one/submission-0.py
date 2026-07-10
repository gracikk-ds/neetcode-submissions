class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        large_int = eval("".join([str(x) for x in digits])) + 1
        digits = []
        while large_int:
            digit = large_int % 10
            large_int //= 10
            digits.append(digit)
        return digits[::-1]