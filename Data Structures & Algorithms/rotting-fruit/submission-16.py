from collections import deque


class Solution:
    # if there is a connected component not containing atleast one rotten fruit,    
    # return -1

    # do a regular bfs and find the max number of "rings" or levels in a single connected component
    # since bfs runs in layers rather than blindly searching one avenue, we can track this by incrementing  counter at a certain point

    # keep only the rotting oranges in the q preloaded. this way we run bfs starting off of a 
    # rotten orange for sure and they dont count as 0/1 nodes anyways. 



    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        
        fresh = 0       # how many fresh oranges in the grid

        q = deque()
        visited = set()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:     # preload visited + q with rottens
                    q.append((r, c, 0))

        # visited: tuples only track row and col number as usual
        # q: tuples also track l, which is distance from last rotten. the maximum of this across the grid, is the answer

                    visited.add((r, c))
                elif grid[r][c] == 1:   # increment fresh counter
                    fresh += 1
              
        longest, fresh_reached = self.bfs(grid, visited, q)

        # modified bfs tells us 1. the longest distance found for a fresh orange from a rotten
        # 2. num of fresh oranges actually reached, so we can compare

        return longest if fresh_reached == fresh else -1
        


        

    def bfs(self, grid, visited, q):
        m = len(grid)
        n = len(grid[0])
        
        longest = 0
        fresh_reached = 0

        while q:
            r, c, l = q.popleft()

            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for d in dirs:
                nr = r + d[0]
                nc = c + d[1]
                nl = l + 1  # track length, +1 at each level

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                if grid[nr][nc] == 0 or (nr, nc) in visited:
                    continue
                
                visited.add((nr, nc))
                q.append((nr, nc, nl))
                longest = max(longest, nl)
                fresh_reached += 1  # if we got here we reached a fresh orange
               
        return longest, fresh_reached
            

            

        