import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # create frequency map for each 
        map = defaultdict(int)
        for num in nums:
            map[num] += 1 
        
        min_heap = [(freq, num) for num, freq in map.items()]

        heapq.heapify(min_heap)


        while len(min_heap) > k:
            heapq.heappop(min_heap)
        
        return [num for freq, num in min_heap]



        