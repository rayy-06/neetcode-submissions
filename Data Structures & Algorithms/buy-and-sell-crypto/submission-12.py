# sliding window: when we care about the actual value of elements between the two bounds
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        min_seen = prices[0]
        res = 0
        for i in range(1, len(prices)):
            # assume we always sell on the day we at and we had bought on min_seen
            # this works since min_seen would have always been before or on the same day
            prof = prices[i] - min_seen

            # update the max profit we are tracking
            res = max(res, prof)

            # update min_seen
            min_seen = min(min_seen, prices[i])
        return res
            
