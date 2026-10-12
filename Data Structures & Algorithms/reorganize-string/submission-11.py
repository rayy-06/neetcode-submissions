import heapq
from collections import deque

class Solution:
    def reorganizeString(self, ss: str) -> str:
        freq = {}
        res = ""

        for s in ss:
            if s not in freq:
                freq[s] = 1
            else:
                freq[s] += 1
        h = []
        for s in freq:
            heapq.heappush(
                h, (-freq[s], s)
            )
        
        q = deque()
        

        while h or q:
            if q:
                front = q[0]
                freq = -front[0]
                char = front[1]

                if char != res[len(res) - 1]:
                    q.popleft()
                    heapq.heappush(h, (-freq, char))
                
                else:
                    if not h:
                        return ""

            if h: 
                popped = heapq.heappop(h)   # we know its elligible no matter what. so pop.
                freq = -popped[0]
                char = popped[1]

            
                #if res == "" or res[len(res) - 1] != char:
                res += char
                freq -= 1
                
                if freq > 0:   
                    q.append((-freq, char))
            
                #if len(h) == 1 and h[0][1] == res[len(res) - 1]:   
                    #return ""
                
        return res

        
        
        

        