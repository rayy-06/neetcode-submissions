import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        result =[]
        l = 0
        r = 0

        while r < len(nums):
            if (r - l + 1) < k:
                heapq.heappush(heap, (-nums[r], r))
                r += 1
            else:
                heapq.heappush(heap, (-nums[r], r))
                cand = heap[0]
                while cand[1] < l:
                    heapq.heappop(heap)
                    cand = heap[0]
                result.append(-heap[0][0])
                l += 1
                r += 1

        return result

        
        

        