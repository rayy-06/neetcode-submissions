class Solution:
    def trap(self, height: List[int]) -> int:
        max_l = 0
        max_r = 0
        l = 0
        r = len(height) - 1
        total = 0
        # at i, trapped is min(max_l, max_r) - height[i]
        # if max_l was used, move it up
        # if max_r was used, bring it down

        # max_l is the largest height l has seen so far.
        # max_r is the same for r
        # why do we need these? if we always use the left boundary instead of max_l, we limit the water contributed on the left side

        while l < r:    
            max_l = max(height[l], max_l)
            max_r = max(height[r], max_r)
            if max_l <= max_r:    
                total += max(max_l - height[l], 0)
                l += 1

            else:
                total += max(max_r - height[r], 0)
                r -= 1
        return total





        