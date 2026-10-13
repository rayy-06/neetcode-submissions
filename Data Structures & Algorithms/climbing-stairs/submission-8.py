class Solution:
    def climbStairs(self, n: int) -> int:
        """

        the naive recurisve implementation says:
        the number of ways to climb to step n is the sum of
        1. the number of ways to climb to (n-1) + 1
        2. the number of ways to climb to (n-2) + 2

        we initialize an array [0, 0, ...0] up to n. then fill it in using dp and return the last element
        """
        if n == 1:
            return 1
        dp = [0] * n
        # there is one distinct way to get to the first step: we start at it
        # there is one distinct way to get to the second step: start at first step, take one step
        dp[0], dp[1] = 1, 2

        for i in range(2, n):
            dp[i] = dp[i-2] + dp[i-1]       
            # reachable from right behind, and reachable from two steps behind. so each number of ways for those two gets added.
        return dp[n-1]
        