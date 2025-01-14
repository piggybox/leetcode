from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # search all possible combinations of coins.
        # as we quickly realize some sub-combinations are repetitive,
        # dynamic programming comes into the play

        # Initialize the minimal coins to reach each amount
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        if dp[amount] != amount + 1:
            return dp[amount]
        else:
            return -1  # no solution
