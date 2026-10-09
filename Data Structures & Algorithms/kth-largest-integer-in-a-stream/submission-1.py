import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        for num in nums:        
            heapq.heappush(self.heap, -num)
        

    def add(self, val: int) -> int:
        heapq.heappush(
            self.heap, -val
        )

        res = []
        for _ in range(self.k - 1):
            res.append(heapq.heappop(self.heap))
        result = -(self.heap[0])

        for num in res:
            heapq.heappush(self.heap, num)

        return result
        
