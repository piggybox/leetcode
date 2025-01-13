from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # super fast implementation using internal set function
        if len(set(nums)) == len(nums):
            return False
        else:
            return True
