class Solution:
    def solveNQueens(self, n):
        cols = set()
        diag = set()
        anti = set()

        board = [['.' for _ in range(n)] for _ in range(n)]
        result = []

        def backtrack(row):
            if row == n:
                result.append([''.join(r) for r in board])
                return

            for col in range(n):
                if (
                    col not in cols and
                    (row - col) not in diag and
                    (row + col) not in anti
                ):
                    board[row][col] = 'Q'
                    cols.add(col)
                    diag.add(row - col)
                    anti.add(row + col)

                    backtrack(row + 1)

                    board[row][col] = '.'
                    cols.remove(col)
                    diag.remove(row - col)
                    anti.remove(row + col)

        backtrack(0)
        return result
    # runtime=11ms  
    #memory=12.64mb