class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        row_l = 0
        row_r = m - 1

        while row_l <= row_r:
            row_m = row_l + (row_r - row_l) // 2
            if target >= matrix[row_m][0] and target <= matrix[row_m][n - 1]:
                # found the row, do binary search in here
                l = 0
                r = n - 1
                while l <= r:
                    m = l + (r-l) // 2     
                    if matrix[row_m][m] == target:       
                        return True

                    elif matrix[row_m][m] < target:
                        l = m + 1     
                    else:
                        r = m - 1
                return False
        
            elif target > matrix[row_m][n - 1]:
                row_l = row_m + 1

            else: # target < matrix[row_m][0]
                row_r = row_m - 1

        return False

        