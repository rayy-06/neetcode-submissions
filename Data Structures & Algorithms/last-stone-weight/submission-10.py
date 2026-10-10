import heapq

class Solution:
    def lastStoneWeight(self, stoness: List[int]) -> int:
        stones = [-stone for stone in stoness]
        heapq.heapify(stones)

        while len(stones) >= 2:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)

            if x < y:
                heapq.heappush(stones, -(y - x))
            
            elif x > y:
                heapq.heappush(stones, -(x - y))
            
        return 0 if len(stones) == 0 else -stones[0]
        