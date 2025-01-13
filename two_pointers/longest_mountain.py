from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        max_mountain = 0
        for i in range(1, len(arr)-1):
            # scan mid point from 1 to n-1
            
            # for each i scan on both sides
            left_size, right_size = 0, 0
            left, right = i - 1, i + 1
            
            while left >= 0:
                if arr[left] < arr[left+1]:
                    left_size += 1
                    left -= 1
                else: 
                    break
        
            while right < len(arr):
                if arr[right] < arr[right-1]:
                    right_size += 1
                    right += 1
                else:
                    break
                
            if left_size > 0 and right_size > 0:
                # there's a mountain
                max_mountain = max(max_mountain, left_size + right_size + 1)
        
        return max_mountain