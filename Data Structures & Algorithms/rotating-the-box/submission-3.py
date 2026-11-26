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
        for i in range(m):
            scan = n - 1
            land = n - 1
            row = matrix[i]
            while scan >= 0:
                if row[scan] == "*":
                    land = scan - 1
                elif row[scan] == "#":
                    row[scan] = "."
                    row[land] = "#"
                    land -= 1
                scan -= 1
            


        
        for i in range(m - 1, -1, -1):  # row number, starting from bottom
            for j in range(n):
                # we are at (i, j) in matrix, which maps to (j, m-1-i) in res
                res[j][m-1-i] = matrix[i][j]
        return res


        