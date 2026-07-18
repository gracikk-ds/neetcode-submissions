class Solution:
    nrows = None
    ncols = None
    destinations = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def borderline(self, row: int, col: int) -> bool:
        if row <= 0 or row >= self.nrows - 1 or col <= 0 or col >= self.ncols - 1:
            return True
        return False

    def solve(self, board: List[List[str]]) -> None:
        self.nrows = len(board)
        self.ncols = len(board[0])

        def dfs(row: int, col: int, is_surround: bool):
            visited.add((row, col))
            region.add((row, col))
            if self.borderline(row, col):
                is_surround = False

            branches = []
            for row_dst, col_dst in self.destinations:
                new_row = row + row_dst
                new_col = col + col_dst
                if (
                    new_row >= 0
                    and new_col >= 0
                    and new_row < self.nrows
                    and new_col < self.ncols
                    and board[new_row][new_col] == "O"
                    and (new_row, new_col) not in visited
                ):
                    branches.append(dfs(new_row, new_col, is_surround))
            is_surround = is_surround and all(branches)

            return is_surround

        # for each possible O rigion run dfs search, skip visited
        visited = set()
        for row in range(self.nrows):
            for col in range(self.ncols):
                if (row, col) in visited:
                    continue
                region = set()
                if board[row][col] == "O":
                    is_surround = dfs(row, col, is_surround=True)
                for rrow, rcol in region:
                    if is_surround:
                        board[rrow][rcol] = "X"
