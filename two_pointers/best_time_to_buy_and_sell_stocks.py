from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Intuition: to maximize profit, we'd like to find the lowest
        # and highest price points in order
        
        # Someone called it Kadane's Algorithm (DP)
        profit = 0 
        buy_price = prices[0]
        
        for right in range(1, len(prices)):
            if buy_price < prices[right]:
                profit = max(profit, prices[right] - buy_price)
            else:
                buy_price = prices[right] # update the lowest price point!

        return profit