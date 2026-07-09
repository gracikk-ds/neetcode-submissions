class Solution:
    def isHappy(self, n: int) -> bool:
        values_set = set()

        while n != 1:

            new_val = 0
            while n:
                digit = n % 10
                new_val += digit**2
                n = n // 10
            n = new_val
            if new_val not in values_set:
                values_set.add(new_val)
                continue
            return False
        return True
