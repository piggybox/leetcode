class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # math trick to get O(n) speed
        return sum(range(len(nums) + 1)) - sum(nums)
