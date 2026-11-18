class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        l = 0
        r = len(heights) - 1
        while l <= r:
            amount = (r - l) * min(heights[l], heights[r])
            result = max(result, amount)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return result
        