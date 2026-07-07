class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first - search for a row
        top = 0
        bot = len(matrix) - 1

        while top <= bot:
            row = (top + bot) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False

        row = (top + bot) // 2
        print(f"{row=}, {target=}")
        left = 0
        right = len(matrix[row]) - 1

        while left <= right:
            middle = (left + right) // 2

            if target > matrix[row][middle]:
                left = middle + 1
            elif target < matrix[row][middle]:
                right = middle - 1
            else:
                return True
        return False

        


        # second - search for a element in the row
        