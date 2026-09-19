class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = []
        cols = []

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)
        
        for row in rows:
            for i in range(n):
                matrix[row][i] = 0
        
        for col in cols:
            for j in range(m):
                matrix[j][col] = 0


        
        