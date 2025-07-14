from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        offset = 1
        
        for i in range(1, n+1):
            # find out cut-off line in 2^x
            if offset * 2 == i:
                offset = i
            
            dp[i] = dp[i-offset] + 1
            
        return dp