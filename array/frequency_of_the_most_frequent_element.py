# Frequency of the Most Frequent Element
# medium

from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        max_count = 0

        for i in nums:
            # find difference
            temp = [x - i for x in nums if x - i >= 0]

            # search distribution of k among difference
            # dynamic programming problem?
            target = k
            count = 0
            for i in temp:
                if k - i > 0:
                    k -= i
                    count += 1

            if count > max_count:
                max_count += count

        return max_count
