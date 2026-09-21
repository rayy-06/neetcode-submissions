from collections import deque

class Solution:
    # IDEA: run a modified BFS which also keeps track of the number of nodes it visited so far. Have it return that value. Loop over all elements in a grid and run BFS on a new compoenent. track the max of the area we are now returning after each rerun of bfs. (OR BFS DOESNT MATTER)


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()

        largest = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (r, c) not in visited:
                    new = self.bfs(grid, r, c, visited)
                    largest = max(largest, new)
        
        return largest




    def bfs(self, grid, r, c, visited):
        m = len(grid)
        n = len(grid[0])

        size = 1

        q = deque()

        visited.add((r, c))
        q.append((r, c))

        while q:
            r, c = q.popleft()
            dirs = [
                (1, 0), (-1, 0), (0, 1), (0, -1)
            ]

            for d in dirs:
                nr = r + d[0]
                nc = c + d[1]

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                
                if grid[nr][nc] == 0 or (nr, nc) in visited:
                    continue
                
                visited.add((nr, nc))
                q.append((nr, nc))

                size += 1
        return size
                





        

        


        

        