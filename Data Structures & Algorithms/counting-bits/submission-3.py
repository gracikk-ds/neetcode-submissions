class Solution:

    def countBits(self, n: int) -> List[int]:
        array = [0 for _ in range(n + 1)]

        for idx in range(n + 1):
            array[idx] = array[idx >> 1] + (idx & 1)
        return array
            
                