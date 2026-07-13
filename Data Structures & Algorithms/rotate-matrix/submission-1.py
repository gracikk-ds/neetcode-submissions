class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # row k -> col n - k - 1
        
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        new_matrix = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

        for row_idx in range(num_rows):
            for col_idx in range(num_cols):
                new_matrix[col_idx][num_cols - row_idx - 1] = matrix[row_idx][col_idx]

        for row_idx in range(num_rows):
            for col_idx in range(num_cols):
                matrix[row_idx][col_idx] = new_matrix[row_idx][col_idx]
