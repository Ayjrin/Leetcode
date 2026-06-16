class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row
        for r in range(9):
            seen = []
            for c in range(9):
                if board[r][c] not in seen and board[r][c] != ".":
                    seen.append(board[r][c])
                elif board[r][c] == ".":
                    continue
                else:
                    return False

        # column
        for c in range(9):
            seen = []
            for r in range(9):
                if board[r][c] not in seen and board[r][c] != ".":
                    seen.append(board[r][c])
                elif board[r][c] == ".":
                    continue
                else:
                    return False

        # grid
        for square in range(9):
            seen = []
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.append(board[row][col])
        return True
















