from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        SIZE = 9  # Board size
        BOX_SIZE = 3  # Sub-boxes size

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(SIZE):
            for j in range(SIZE):
                cur = board[i][j]
                
                if cur == '.':
                    continue

                # Use tuple (row, col) to identify each box
                box_key = (i//3, j//3)
                
                if cur in rows[i] or cur in cols[j] or cur in boxes[box_key]:
                    return False
                
                rows[i].add(cur)
                cols[j].add(cur)
                boxes[box_key].add(cur)
        
        return True