class Solution:
    def rotateTheBox(self, matrix: List[List[str]]) -> List[List[str]]:
        m = len(matrix)
        n = len(matrix[0])

        res = []
        for i in range(n):
            res.append(
                ["."] * m
            )

        # handle gravity first in the original matrix, row by row
        for i in range(m):  # loop over each row plainly
            scan = n - 1    # scan iterates on the row in reverse
            land = n - 1    # land marks where the rock found by scan will go
            row = matrix[i]
            while scan >= 0:    # we want to apply gravity to each row before transposing
                if row[scan] == "*":
                    # we cannot place a rock here. so the land index goes behind this
                    land = scan - 1
                elif row[scan] == "#":
                    # make the swap, and now land is taken so move it back
                    row[scan] = "."
                    row[land] = "#"
                    land -= 1
                scan -= 1
            


        
        for i in range(m - 1, -1, -1):  # row number, starting from bottom
            for j in range(n):
                # we are at (i, j) in matrix, which maps to (j, m-1-i) in res
                res[j][m-1-i] = matrix[i][j]
        return res


        