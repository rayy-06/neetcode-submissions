class Solution:
    def trap(self, height: List[int]) -> int:
        max_l = 0
        max_r = 0
        l = 0
        r = len(height) - 1

        total = 0

        while l < r:    # in two pointer, the condition is always in terms of pointers
            max_l = max(height[l], max_l)
            max_r = max(height[r], max_r)

            if max_l <= max_r: # min of the two is the left one
                # then, add on the height of current using left as anchor and increment left since we are done with it
                total += max(max_l - height[l], 0)
                l += 1

            else:
                total += max(max_r - height[r], 0)
                r -= 1
        return total


        