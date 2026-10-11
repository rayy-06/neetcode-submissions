import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # create a min heap using tuples where the first element is the distance and the second element is the point itself. 
        heap = []
        for point in points:    # x1, y1 = [0, 0]
            dist = math.sqrt(   # x2, y2 = [point[0], point[1]]  
                (point[0])**2 + (point[1])**2
                )
            heapq.heappush(
                heap, (dist, point)
            )
        
        result = []
        for _ in range(k):
            result.append(
                heapq.heappop(heap)[1]
            )
        
        return result


        