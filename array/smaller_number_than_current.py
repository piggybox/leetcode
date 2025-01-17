from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # standard solution. There's a tricky O(n) solution but that's like a
        # brain teaser
        sorted_num = sorted(nums)

        index = {}
        for i, v in enumerate(sorted_num):
            if i not in index:
                index[v] = i

        res = []
        for v in nums:
            res.append(index[v])

        return res
