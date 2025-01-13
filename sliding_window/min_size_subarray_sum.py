from typing import List 

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums)
        total = 0

        if sum(nums) < target:
            return 0

        # dynamic sliding window
        left  = 0
        
        # it's important to check through all possible right
        for right in range(len(nums)): 
            # accumulate right until total is bigger than target
            total += nums[right]
            
            # then try to shrink the left side
            while total >= target:
                res = min(res, right - left +1)
                total -= nums[left]
                left += 1

        return res
