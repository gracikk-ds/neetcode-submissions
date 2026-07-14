class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(word)
        num_rows = len(board)
        num_cols = len(board[0])
        res, sol = [], []
        visited = set()

        def backtrack(row_idx: int, col_idx: int) -> None:
            if not "".join(sol) == word[: len(sol)]:
                return 

            if "".join(sol) == word:
                res.append("".join(sol))
                return

            # go left
            if col_idx - 1 >= 0:
                if (row_idx, col_idx - 1) not in visited:
                    visited.add((row_idx, col_idx - 1))
                    sol.append(board[row_idx][col_idx - 1])
                    backtrack(row_idx, col_idx - 1)
                    sol.pop()
                    visited.remove((row_idx, col_idx - 1))

            # go right
            if col_idx + 1 < num_cols:
                if (row_idx, col_idx + 1) not in visited:
                    visited.add((row_idx, col_idx + 1))
                    sol.append(board[row_idx][col_idx + 1])
                    backtrack(row_idx, col_idx + 1)
                    sol.pop()
                    visited.remove((row_idx, col_idx + 1))

            # go down
            if row_idx + 1 < num_rows:
                if (row_idx + 1, col_idx) not in visited:
                    visited.add((row_idx + 1, col_idx))
                    sol.append(board[row_idx + 1][col_idx])
                    backtrack(row_idx + 1, col_idx)
                    sol.pop()
                    visited.remove((row_idx + 1, col_idx))

            # go up
            if row_idx - 1 >= 0:
                if (row_idx - 1, col_idx) not in visited:
                    visited.add((row_idx - 1, col_idx))
                    sol.append(board[row_idx - 1][col_idx])
                    backtrack(row_idx - 1, col_idx)
                    sol.pop()
                    visited.remove((row_idx - 1, col_idx))

        for row in range(num_rows):
            for col in range(num_cols):
                if res:
                    break
                if board[row][col] == word[0]:
                    visited.add((row, col))
                    sol.append(board[row][col])
                    backtrack(row, col)
                    sol.pop()
                    visited.remove((row, col))

        return True if res else False
