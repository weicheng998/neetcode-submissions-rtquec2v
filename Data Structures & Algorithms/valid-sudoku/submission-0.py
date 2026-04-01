class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        num_rows = 9
        num_cols = 9

        # Check if rows valid
        for i in range(num_rows):
            row_list = []
            for j in range(num_cols):
                cur = board[i][j]
                if cur != '.':
                    row_list.append(cur)
            if len(row_list) != len(set(row_list)):
                return False
        
        # Check if cols valid
        for i in range(num_cols):
            col_list = []
            for j in range(num_rows):
                cur = board[j][i]
                if cur != '.':
                    col_list.append(cur)
            if len(col_list) != len(set(col_list)):
                return False
        
        # Check if sub-boxes valid
        sb_len = int(num_rows/3)
        # i - [0, 3, 6]
        for i in range(0, num_cols, sb_len):
            # j - [0, 3, 6]
            for j in range(0, num_rows, sb_len):
                sb_list = []
                for a in range(sb_len):
                    for b in range(sb_len):
                        cur = board[i+a][j+b]
                        if cur != '.':
                            sb_list.append(cur)
                if len(sb_list) != len(set(sb_list)):
                    return False
        
        # All three rules are satisfied
        return True
        