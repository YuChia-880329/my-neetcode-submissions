class Solution:

    _DELIMITER = '.'
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        k = int(n ** 0.5)

        # hash tables
        row_check = [set() for _ in range(n)]
        col_check = [set() for _ in range(n)]
        grid_check = [set() for _ in range(n)]

        for i in range(n):
            for j in range(n):
                slot = board[i][j]
                if slot != Solution._DELIMITER:
                    grid_index = i//k * k + j//k
                    # check
                    if (slot in row_check[i]) or (slot in col_check[j]) or (slot in grid_check[grid_index]):
                        return False

                    # update
                    row_check[i].add(slot)
                    col_check[j].add(slot)
                    grid_check[grid_index].add(slot)

        return True
