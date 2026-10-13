class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)

        # base cases

        if amount == 0:
            return 0

        if amount == 1 and 1 in coins:
            return 1
        else:
            if amount == 1:
                return -1
        
        if len(coins) == 1 and (coins[0] > amount or amount % coins[0] != 0):
            return -1
        
        dp[0] = 0
        dp[1] = 1 if 1 in coins else -1

        for i in range(2, amount + 1):  # each i is the amount we are trying to construct
            minimum = float('inf')
            found = False
            for coin in coins:
                if coin == i:
                    minimum = 1
                    found = True
                    break

                if coin <= i and i - coin >= 0 and dp[i - coin] >= 0:
                    minimum = min(minimum, dp[i - coin] + 1)
                    found = True
            dp[i] = minimum if found else -1
        return dp[amount]

        