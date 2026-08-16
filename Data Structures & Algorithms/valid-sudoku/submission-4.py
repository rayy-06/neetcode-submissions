class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # rows[i] is a set tracking all of the valid numbers seen in row[i] so far.
        # same with cols and boxes. it does the same as a dict.

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                
                # if we consider a box row and box col:
                b_row = i//3
                b_col = j//3
                
                # so , we can map a coord to a box coord. for box coord to an index from
                # 0-8...

                b = b_row * 3 + b_col

                # skip 3 for each advanced row, add one col at a time

                if val in rows[i] or val in cols[j] or val in boxes[b]:
                    return False
                
                rows[i].add(val)
                cols[j].add(val)
                boxes[b].add(val)
        return True
        