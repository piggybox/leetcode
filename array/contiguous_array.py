class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count_map = {0: -1} # position of the first occurrence of each count
        max_length = 0
        count = 0

        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1 # prefix sum logic
            
            if count in count_map:
                # If the prefix sum at two indices is the same, 
                # it means that the number of 0s and 1s between those two indices is the same!
                max_length = max(max_length, i - count_map[count])
            else:
                count_map[count] = i
        
        return max_length