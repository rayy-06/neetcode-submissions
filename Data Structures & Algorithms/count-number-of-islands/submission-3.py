
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        islands = 0     # connected components

        for r in range(m):
            for c in range(n):
                if (r, c) not in visited and grid[r][c] == "1":
                    islands += 1
                    self.bfs(grid, r, c, visited)

        return islands



    def dfs(self, grid, r, c, visited):  
        # think of the grid as an m x n matrix of 0 and 1 where 1 represents a node and 0 is empty space
        # Then, the matrix contains a certain number of connected componenets.
        m = len(grid)    
        n = len(grid[0])

        if r < 0 or r >= m or c < 0 or c >= n:    # bounds checks for r (row number) and c (col number)
            return

        if grid[r][c] == "0" or (r, c) in visited:    # skip any 0s, or 1s that are visited already
            return

        visited.add(
            (r, c)
            )       # ready to visit the current node

        self.dfs(grid, r + 1, c, visited)       # recurse in each direction off of (r, c)
        self.dfs(grid, r - 1, c, visited)       # up, left, down, right. 
        self.dfs(grid, r, c + 1, visited)
        self.dfs(grid, r, c - 1, visited)       # same visited passed throughout maintains the state

        # DFS will run only as long as it is within a connected component. When it sees a 0 it stops    
        #even when all connected compoenents in the grid were not visited yet.



    def bfs(self, grid, r, c, visited):
        # BFS uses LIFO, queue to visit each node iterativley
        # BFS always finds the shortest path from one node to another.
        q = deque()
        m = len(grid)
        n = len(grid[0])

        q.append((r, c))        # queue is used for processing. visited holds the same function
        visited.add((r, c))

        while q:
            r, c = q.popleft()  # pop the element to be processed

            dirs = [
                (1, 0), (-1, 0), (0, 1), (0, -1)
            ]

            for d in dirs:      # loop in each direction (equivalent to recursing in each dir)
                new_row = r + d[0]
                new_col = c + d[1]

                if new_row < 0 or new_row >= m or new_col < 0 or new_col >= n:
                    continue        # same checks as dfs (bounds and then 0, or 1 which is visited)

                if grid[new_row][new_col] == "0" or (new_row, new_col) in visited:
                    continue
                
                # in both cases continue, so loop to next iter (equivalent to return)

                visited.add((new_row, new_col)) # if we get here this is valid unvisited node.
                q.append((new_row, new_col))










        