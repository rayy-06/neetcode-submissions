import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        m = max(piles)
        best = m

        l = 1
        r = m

        while l <= r:        
            mid = l + (r-l) // 2
            time = h

            # start a trial
            for b in piles:
                h_needed = math.ceil(b / mid)
                time -= h_needed

                if time < 0:
                    break
            if time < 0:
                # trial failed
                l = mid + 1
            else:   # it worked (time was >= 0), find a smaller mid
                best = min(mid, best)
                r = mid - 1
        
        return best




                
                
                
                
                





            


        