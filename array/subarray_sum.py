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

        # this works but not scalable
        # for i in range(len(prefix_sum)):
        #     if prefix_sum[i] == k:
        #         count += 1

        #     for j in range(i):
        #         if prefix_sum[i] - prefix_sum[j] == k:
        #             count += 1

        # more scalable way: use a hash map to store the prefix sum and count
        prefix_sum_map = {0:1} # very important to initialize the euqal case!

        for sum in prefix_sum:
            if (sum - k) in prefix_sum_map:
                count += prefix_sum_map[sum - k]
            
            if sum in prefix_sum_map:
                prefix_sum_map[sum] += 1
            else:
                prefix_sum_map[sum] = 1

        return count
        
