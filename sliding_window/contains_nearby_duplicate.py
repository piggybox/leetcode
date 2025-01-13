from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # alternative we can maintain a fixed length set as sliding window
        seen = {} # num => index
        
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            else:
                seen[num] = i # update the index to the latest seen
                
        return False