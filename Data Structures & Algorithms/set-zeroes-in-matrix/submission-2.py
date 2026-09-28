class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = []
        cols = []

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):  # traverse the whole matrix. if we hit a 0, save that row and col as a "need to be zeroed out" row/col
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)
        
        # when we have our rows and cols, zero each out by iterating
        for row in rows:
            for i in range(n):
                matrix[row][i] = 0  # use direct indeces to change in place. for num in row creates temp vars and does not save the change
        
        for col in cols:
            for j in range(m):
                matrix[j][col] = 0


        
        