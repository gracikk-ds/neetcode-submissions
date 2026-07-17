class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        destinations: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        num_rows: int = len(heights)
        num_cols: int = len(heights[0])

        points: list[list[int]] = []
        for row in range(num_rows):
            for col in range(num_cols):
                visited = set()
                ocean_collection = set()
                queue = deque()
                queue.append((row, col))
                visited.add((row, col))

                while queue and len(ocean_collection) < 2:
                    for _ in range(len(queue)):
                        last_row, last_col = queue.popleft()

                        if last_row < 0 or last_col < 0:
                            ocean_collection.add("pacific")
                        elif last_row >= num_rows or last_col >= num_cols:
                            ocean_collection.add("atlantic")
                        else:
                            for row_dst, col_dst in destinations:
                                new_col = last_col + col_dst
                                new_row = last_row + row_dst

                                if (new_row, new_col) in visited:
                                    continue

                                if (
                                    new_col >= 0
                                    and new_row >= 0
                                    and new_col < num_cols
                                    and new_row < num_rows
                                    and heights[new_row][new_col] > heights[last_row][last_col]
                                ):
                                    continue
                                queue.append((new_row, new_col))
                                visited.add((new_row, new_col))
                        if len(ocean_collection) == 2:
                            points.append([row, col])
                            break

        return points
