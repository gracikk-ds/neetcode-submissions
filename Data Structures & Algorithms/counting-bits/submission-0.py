class Solution:

    def countBits(self, n: int) -> List[int]:
        array = [0 for _ in range(n + 1)]

        for idx, val in enumerate(range(n + 1)):
            count = 0
            while val:
                count += val % 2
                val = val >> 1
            array[idx] = count
        return array
            
                