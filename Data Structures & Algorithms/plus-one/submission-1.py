class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        large_int: int = 0
        length = len(digits) - 1
        for digit in digits:
            large_int += digit * 10**length
            length -= 1

        large_int += 1
        digits = []
        while large_int:
            digits.append(large_int % 10)
            large_int //= 10

        return digits[::-1]