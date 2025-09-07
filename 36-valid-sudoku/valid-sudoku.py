class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        d = set()
        for i in range(n):
            for j in range(n):
                b = board[i][j]
                if b != '.':
                    if (b, i, -1) in d or (b, -1, j,) in d or (b, i // 3, j // 3) in d:
                        return False
                    d.add((b, i, -1))
                    d.add((b, -1, j))
                    d.add((b, i // 3, j // 3))
        return True