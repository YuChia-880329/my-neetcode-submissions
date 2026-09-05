from math import sqrt
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        k = int(sqrt(n))
        row_record = [set() for _ in range(n)]
        col_record = [set() for _ in range(n)]
        grid_record = [set() for _ in range(n)]

        for i in range(n):
            for j in range(n):
                num = int(board[i][j]) if board[i][j].isdigit() else None
                if num != None:
                    # check
                    grid_num = i//k * k + j//k
                    if (num in row_record[i]) or (num in col_record[j]) or (num in grid_record[grid_num]):
                        return False
                    # update
                    row_record[i].add(num)
                    col_record[j].add(num)
                    grid_record[grid_num].add(num)

        return True
