# 560. Subarray Sum Equals K

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # build up a prefix sum
        prefix_sum = []
        for num in nums:
            if not prefix_sum:
                prefix_sum.append(num)
            else:
                prefix_sum.append(prefix_sum[-1] + num)
        
        # find the subarray
        count = 0

        for i in range(len(prefix_sum)):
            if prefix_sum[i] == k:
                count += 1

            for j in range(i):
                if prefix_sum[i] - prefix_sum[j] == k:
                    count += 1

        return count
        
