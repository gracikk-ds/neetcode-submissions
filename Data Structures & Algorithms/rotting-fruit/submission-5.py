class Solution:
    destinations: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def isvalid(
        self,
        grid: List[List[int]],
        row: int,
        col: int,
        num_rows: int,
        num_cols: int,
    ) -> bool:
        if (
            row < 0
            or row >= num_rows
            or col < 0
            or col >= num_cols
            or grid[row][col] != 1
        ):
            return False
        return True

    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_minutes: int = 0
        num_rows = len(grid)
        num_cols = len(grid[0])

        rotten_fruits: list[tuple[int, int]] = []
        fresh: int = 0
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 2:
                    rotten_fruits.append((row, col))
                if grid[row][col] == 1:
                    fresh += 1

        if not fresh:
            return 0

        queue = deque(rotten_fruits)

        while queue and fresh:
            num_minutes += 1
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for row_dst, col_dst in self.destinations:
                    next_row = row + row_dst
                    next_col = col + col_dst
                    if self.isvalid(grid, next_row, next_col, num_rows, num_cols):
                        grid[next_row][next_col] = 2
                        fresh -= 1
                        queue.append((next_row, next_col))

        return num_minutes if not fresh else -1
