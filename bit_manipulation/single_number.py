from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash = {}
        for i in range(len(nums)):
            if nums[i] in hash:
                hash[nums[i]] += 1
            else:
                hash[nums[i]] = 1

        for k, v in hash.items():
            if v == 1:
                return k

    # alternative solution with xor manipulation with O(1) space
        xor = 0
        for i in nums:
            xor ^= i 
        return xor
    