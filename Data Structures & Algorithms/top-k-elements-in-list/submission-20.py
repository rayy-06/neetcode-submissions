import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a frequency dictionary
        f_map = {}
        for num in nums:
            if num not in f_map:
                f_map[num] = 1
            else:
                f_map[num] += 1
        
        heap = []
        for num in f_map:
            heapq.heappush(heap, (-f_map[num], num))
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

        