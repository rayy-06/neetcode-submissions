class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # sliding window: we care about two metrics and also what is in between them
        # the fact that we care about what is in between, is the main differentiator
        # between two pointer and sliding window.

        # we want to buy at the cheapest. so as we iterate keep track of the cheapest 
        # day we have seen so far and calculate what the profit would be if we sold at the given day. So we want minimum sell day and max profit tracked at the same time

        min_price = prices[0]
        max_profit = 0
        for p in prices:
            profit = p - min_price
            max_profit = max(profit, max_profit)

            min_price = min(min_price, p)

        return max_profit
        