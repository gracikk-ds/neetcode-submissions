class Solution:
    destinations = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        num_rows: int = len(heights)
        num_cols: int = len(heights[0])

        def dfs(row: int, col: int) -> None:  # check if None correct
            if (row, col) in visited:
                return

            if len(oceans_reached) == 2:
                return

            if row < 0 or col < 0:
                return "pacific"

            if row >= num_rows or col >= num_cols:
                return "atlantic"

            visited.add((row, col))

            for row_dst, col_dst in self.destinations:
                next_row = row + row_dst
                next_col = col + col_dst

                if (
                    next_row >= 0
                    and next_col >= 0
                    and next_row < num_rows
                    and next_col < num_cols
                    and heights[next_row][next_col] > heights[row][col]
                ):
                    continue

                ocean_type = dfs(next_row, next_col)
                if ocean_type is not None:
                    oceans_reached.add(ocean_type)

        output = []
        for row in range(num_rows):
            for col in range(num_cols):
                visited = set()
                oceans_reached = set()
                dfs(row, col)
                if len(oceans_reached) == 2:
                    output.append([row, col])
        return output
