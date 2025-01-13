from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        max_mountain = 0
        # TODO optimization: can skip a few descending items as they can't be the next mid point
        for i in range(1, len(arr)-1):
            # check minimal condition for a mountain
            if arr[i-1] < arr[i] > arr[i+1]:
                # for each i scan on both sides
                left, right = i - 1, i + 1
                
                while left >= 0 and arr[left] < arr[left+1]:
                    left -= 1

            
                while right <= len(arr) and arr[right] < arr[right-1]:
                    right += 1

                # -2 as the final step of while loop does one extra movement
                # alternatively, we can initialize left and right with i on L11
                max_mountain = max(max_mountain, right - left + 1 - 2) 
                #print(i, max_mountain)
        
        return max_mountain