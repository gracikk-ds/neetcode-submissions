class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # get all elements from left to right at the top
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # get all elements from top to bottom in the right
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            # get all elements from right to left in the bottom
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1     

            # get all elements from bottom to top in the left
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1     
              
        return res