class Solution:
    def spiralOrder(self, grid: List[List[int]]) -> List[int]:
        left = 0
        right = len(grid[0]) - 1
        up = 0
        down = len(grid) - 1

        res = []

        while left <= right and up <= down:
            for i in range(left, right + 1):    # row at up
                res.append(grid[up][i])
            up += 1

            for i in range(up, down + 1):   # col at right
                res.append(grid[i][right])
            right -= 1

            if down >= up:
                for i in range(right, left - 1, -1):    # row at down, if it exists
                    res.append(grid[down][i])
                down -= 1
            
            if left <= right:
                for i in range(down, up - 1, -1):   # col at left, if it exists
                    res.append(grid[i][left])
                left += 1
        return res


        