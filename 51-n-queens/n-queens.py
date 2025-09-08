class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results: List[List[str]] = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        cols = set()       # occupied columns: c
        diags = set()      # occupied main diagonals: r - c
        antiDiags = set()  # occupied anti-diagonals: r + c

        def backtrack(row: int) -> None:
            if row == n:
                results.append([''.join(r) for r in board])
                return

            # Try placing a queen in each column of this row
            for col in range(n):
                if (col in cols) or ((row - col) in diags) or ((row + col) in antiDiags):
                    continue  # unsafe position, skip

                # Choose: place queen and mark constraints
                board[row][col] = 'Q'
                cols.add(col)
                diags.add(row - col)
                antiDiags.add(row + col)

                backtrack(row + 1)
                
                # Un-choose: remove queen and unmark constraints
                board[row][col] = '.'
                cols.remove(col)
                diags.remove(row - col)
                antiDiags.remove(row + col)
        backtrack(0)
        return results