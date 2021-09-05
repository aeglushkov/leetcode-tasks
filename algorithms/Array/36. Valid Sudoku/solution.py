class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        unique_sub_boxes = [[[], [], []] for i in range(3)]
        for i in range(9):
            row_unique = dict()
            col_unique = dict()
            for j in range(9):
                if board[i][j] != ".":
                    if row_unique.get(board[i][j]) is not None:
                        return False
                    row_unique[board[i][j]] = board[i][j]
                    if board[i][j] in unique_sub_boxes[i // 3][j // 3]:
                        return False
                    unique_sub_boxes[i // 3][j // 3].append(board[i][j])
                if board[j][i] != ".":
                    if col_unique.get(board[j][i]) is not None:
                        return False
                    col_unique[board[j][i]] = board[j][i]
        return True
