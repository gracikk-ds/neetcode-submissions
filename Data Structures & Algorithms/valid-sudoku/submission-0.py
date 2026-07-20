class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_hashmap = defaultdict(set)
        cols_hashmap = defaultdict(set)
        square_hasmap = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[0])):
                # skip empty cells
                if board[row][col] == ".":
                    continue
                
                # check row
                if board[row][col] in rows_hashmap[row]:
                    return False
                rows_hashmap[row].add(board[row][col])

                # check col
                if board[row][col] in cols_hashmap[col]:
                    return False
                cols_hashmap[col].add(board[row][col])

                # check square
                if board[row][col] in square_hasmap[(row // 3, col // 3)]:
                    return False
                square_hasmap[(row // 3, col // 3)].add(board[row][col])
        return True
                
