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
        for num in f_map:   # pushing only k elements vs all n
            heapq.heappush(heap, (f_map[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        while heap: # then, empty out the k instead of popping k times.
            res.append(heapq.heappop(heap)[1])
        return res
