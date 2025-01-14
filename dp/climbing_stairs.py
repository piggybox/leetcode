class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        # dp[3] = 3

        for i in range(3, n + 1):
            # 1 step for dp[i-1] or 2 steps for dp[i-2]
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
