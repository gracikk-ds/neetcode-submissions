class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def dfs(row: int, col: int):
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or (row, col) in visited
                or grid[row][col] == "0"
            ):
                return 0 

            visited.add((row, col))
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

            return 1

        num_islands = 0
        for row in range(rows):
            for col in range(cols):
                num_islands += dfs(row, col)
        return num_islands
