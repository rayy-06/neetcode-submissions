class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        m = len(matrix)
        n = len(matrix[0])

        top, bottom = 0, m - 1
        left, right = 0, n - 1

        while left <= right and top <= bottom:
            for i in range(left, right + 1):    # top row 
                result.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):   # right COL 
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):   # bottom row 
                    result.append(matrix[bottom][i])
                bottom -= 1
            
            if left <= right:
                for i in range(bottom, top - 1, -1):   # left col
                    result.append(matrix[i][left])
                left += 1
            
        
        return result






        
        