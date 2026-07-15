class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        max_area = 0

        def bfs(row: int, col: int) -> int:
            queue = deque()
            queue.append((row, col))
            visited.add((row, col))
            area = 1

            while queue:
                queue_len = len(queue)

                for _ in range(queue_len):
                    row, col = queue.popleft()

                    for dr, dc in directions:
                        row_d = row + dr
                        col_d = col + dc
                        if (
                            row_d < 0
                            or row_d >= rows
                            or col_d < 0
                            or col_d >= cols
                            or (row_d, col_d) in visited
                            or grid[row_d][col_d] == 0
                        ):
                            continue
                        visited.add((row_d, col_d))
                        queue.append((row_d, col_d))
                        area += 1
            return area

        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and grid[row][col] == 1:
                    max_area = max(bfs(row, col), max_area)

        return max_area
