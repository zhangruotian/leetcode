class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        subbox_set =[[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                subbox_i,subbox_j = i//3,j//3
                if cell in row_set[i] or cell in col_set[j] or cell in subbox_set[subbox_i][subbox_j]:
                    return False
                if cell.isdigit():
                    row_set[i].add(cell)
                    col_set[j].add(cell)
                    subbox_set[subbox_i][subbox_j].add(cell)
        return True
