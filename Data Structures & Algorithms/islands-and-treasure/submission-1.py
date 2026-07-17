class Solution:
    num_rows: Optional[int] = None
    num_cols: Optional[int] = None
    destinations: list[tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def destination_isvalid(
        self, grid: List[List[int]], visited: set[int], row: int, col: int
    ) -> bool:
        if (
            row >= 0
            and row < self.num_rows
            and col >= 0
            and col < self.num_cols
            and grid[row][col] != -1
            and (row, col) not in visited
        ):
            return True
        return False

    def bfs(self, grid: List[List[int]], row: int, col: int) -> int:
        queue = deque()
        queue.append((row, col))
        visited = set()
        visited.add((row, col))

        min_path = 0
        while queue:
            for _ in range(len(queue)):
                new_row, new_col = queue.popleft()

                if grid[new_row][new_col] == 0:
                    return min_path

                for row_dts, col_dst in self.destinations:
                    if self.destination_isvalid(grid, visited, new_row + row_dts, new_col + col_dst):
                        queue.append((new_row + row_dts, new_col + col_dst))
                        visited.add((new_row + row_dts, new_col + col_dst))
            min_path += 1

        return grid[row][col]

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.num_rows = len(grid)
        self.num_cols = len(grid[0])

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if grid[row][col] != -1 and grid[row][col] != 0:
                    grid[row][col] = self.bfs(grid, row, col)
