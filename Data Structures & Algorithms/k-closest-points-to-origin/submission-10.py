import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # use a heap with tuples (distance, [x, y])
        # heapq is a min heap by default so we get the closest points (smallest distance)
        # as we wish
        heap = []
        for point in points:
            d = (math.sqrt((point[0])**2 + (point[1])**2))
            heapq.heappush(heap, (d, point))

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

        