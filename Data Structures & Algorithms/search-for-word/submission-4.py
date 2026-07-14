class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        num_rows, num_cols = len(board), len(board[0])
        n = len(word)
        visited = set()

        def backtrack(row: int, col: int, idx: int) -> None:
            if idx == n:
                return True
            if (row < 0 or row >= num_rows or col < 0 or col >= num_cols
                    or (row, col) in visited
                    or board[row][col] != word[idx]):
                return False

            visited.add((row, col))

            found = (
                backtrack(row + 1, col, idx + 1) or
                backtrack(row - 1, col, idx + 1) or
                backtrack(row, col + 1, idx + 1) or
                backtrack(row, col - 1, idx + 1)
            )

            visited.remove((row, col))
            return found

        for row in range(num_rows):
            for col in range(num_cols):
                if board[row][col] == word[0] and backtrack(row, col, 0):
                    return True

        return False
