class Solution:
    destinations: list[tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    num_rows: Optional[int] = None
    num_cols: Optional[int] = None

    def isvalid(
        self,
        grid: List[List[int]],
        visited: set(tuple[int, int]),
        row: int,
        col: int,
    ) -> bool:
        if self.num_rows is None or self.num_cols is None:
            return False

        if (
            row >= 0
            and row < self.num_rows
            and col >= 0
            and col < self.num_cols
            and (row, col) not in visited
            and grid[row][col] != -1
        ):
            return True
        return False

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.num_rows = len(grid)
        self.num_cols = len(grid[0])

        list_of_gates = []
        visited = set()
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if grid[row][col] == 0:
                    list_of_gates.append((row, col))
                    visited.add((row, col))

        queue = deque(list_of_gates)
        length: int = 1
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dst_row, dst_col in self.destinations:
                    new_row, new_col = row + dst_row, col + dst_col
                    if self.isvalid(grid, visited, new_row, new_col):
                        grid[new_row][new_col] = length
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))
            length += 1

