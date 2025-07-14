from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        for i in range(n):
            # If the previous sum is negative, we just start it over
            # If not, we can add the current number
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        return max(dp)
